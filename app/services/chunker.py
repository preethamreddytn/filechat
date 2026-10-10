from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter=RecursiveCharacterTextSplitter( 

    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n","\n","."," ",",","\t"]


)
def chunk_document(text):
    chunks=text_splitter.split_documents(text)

    chunks=[
        chunk for chunk in chunks if chunk.page_content.strip()
    ]

    return chunks

