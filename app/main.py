from fastapi import FastAPI , Request, UploadFile, File , Form
from fastapi.templating import Jinja2Templates
import tempfile
from os import remove


from app.services.file_processer import text_extraction
from app.services.chunker import chunk_document
from app.services.vector_store import create_vector_store , similarity_search
from app.services.ask_model import ask_model

app=FastAPI()
templates=Jinja2Templates(directory='app/templates')

vector_store=None
uploaded_filename=None



@app.get('/')
def home(request : Request):
    return templates.TemplateResponse('home.html',{'request':request})




@app.post('/')
async def upload_file(request: Request,file: UploadFile=File(...)):
    global vector_store,uploaded_filename
    file_path=None

    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(await file.read())
            file_path = temp.name

        text=text_extraction(file_path,file.content_type)
        chunks=chunk_document(text)

        new_vector_store=create_vector_store(chunks)

        vector_store = new_vector_store
        if not vector_store:
            return templates.TemplateResponse('home.html',{'request':request,'error':'document is empty ,enter proper document and try again'})
        uploaded_filename = file.filename
        return templates.TemplateResponse(
            "home.html",
            {
                "request": request,
                "filename": uploaded_filename,
                "number_chunks": len(chunks),
                "vector_store_ready": True
            }
        )


    finally:
        if file_path:
            import os
            os.remove(file_path)




@app.post('/ask')
async def ask_question(request: Request , question:str=Form(...)):
    if not vector_store :
        
  
        return templates.TemplateResponse('home.html',{'request':request,'error':'document is empty or question is null'})
    context = similarity_search(vector_store, question)

    result=ask_model(question,context)



    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "filename": uploaded_filename,
            "vector_store_ready": True,
            "question": question,
            "results": result
        })