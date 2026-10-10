from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key="AIzaSyApxLa1N3ijqiS53LxeNA4fQK9A6RR8rdk")

def ask_model(question,context):
    prompt=f"""answer the following question: {question}: based on the context: {context} ..answer the question if answer present incontext else say answer is not present in file """
    try:
        result=model.invoke(prompt)
        if result.content:
            return result.content
    except Exception as e:
        return "answer is not in this file or backend error occured please try again"