# FileChat

FileChat is a lightweight document Q&A web application built with FastAPI. It lets you upload a PDF, DOCX, or TXT file, extract its text, split it into chunks, index the content with a vector store, and then ask questions about the uploaded document.

## Features

- Upload PDF, DOCX, and TXT documents
- Extract and chunk document content
- Generate embeddings with Hugging Face models
- Store and search chunks with FAISS
- Ask questions using a Gemini-powered model
- Web UI built with Jinja templates and custom CSS

## Tech Stack

- Python
- FastAPI
- Jinja2
- LangChain
- FAISS
- Hugging Face embeddings
- Google Generative AI

## Project Structure

```text
filechat/
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── ask_model.py
│   │   ├── chunker.py
│   │   ├── file_processer.py
│   │   └── vector_store.py
│   └── templates/
│       ├── home.css
│       └── home.html
├── .gitignore
├── README.md
├── requirements.txt
└── .env.example (optional, add if you use environment variables)
```

## How it Works

1. A file is uploaded through the FastAPI UI.
2. The app extracts text from the document.
3. The text is split into smaller chunks.
4. Embeddings are created for each chunk.
5. A FAISS vector store is created for similarity search.
6. When a user asks a question, the app retrieves the most relevant chunks and sends them to the LLM for an answer.

## Prerequisites

- Python 3.10+
- pip
- A valid Google Generative AI API key

## Installation

Clone the repository:

```bash
git clone https://github.com/preethamreddytn/filechat.git
cd filechat
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up your environment variables. The app loads a `.env` file and the generative model integration expects a valid Gemini API key.

```bash
# .env
GOOGLE_API_KEY=your_api_key_here
```

If your local code is using a hardcoded key in `app/services/ask_model.py`, make sure it is updated to use the key from your environment or your own secure configuration.

## Running the App

Start the server:

```bash
uvicorn app.main:app --reload
```

Then open your browser at:

```text
http://localhost:8000
```

Upload a supported file and ask a question about it.

## Supported File Types

- PDF
- DOCX
- TXT

## Notes

This project is useful for quick document exploration and local RAG-style querying. It is a simple prototype and can be extended with better UI improvements, authentication, persistent storage, and more robust document parsing.

## License

This project does not currently include a license file. If needed, add one before publishing or sharing it publicly.
