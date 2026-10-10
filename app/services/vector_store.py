from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def embedding_model():
    return HuggingFaceEmbeddings(
        model="ibm-granite/granite-embedding-311m-multilingual-r2"
    )


def create_vector_store(chunks):
    if not chunks:
        return None
    embeddings=embedding_model()

    vector_store=FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


def similarity_search(vector_store,question,k_value=3):

    results=vector_store.similarity_search(
        question,
        k=k_value
    )

    return results