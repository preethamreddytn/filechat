from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader


def text_extraction(file,extension):
    

    if extension=='application/pdf':
        loader=PyPDFLoader(file)

    elif extension=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        loader=Docx2txtLoader(file)

    elif extension=='text/plain':
        loader=TextLoader(file)

    else:
        raise ValueError('File not supported')

    return loader.load()






    