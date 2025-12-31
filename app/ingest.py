import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

DATA_DIR = "data/sample_docs"
VECTOR_STORE_DIR = "vector_store"

def ingest_documents():
    documents = []

    for file in os.listdir(DATA_DIR):
        if file.lower().endswith(".pdf"):
            path = os.path.join(DATA_DIR, file)
            print(f"Loading {path}")
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

    if not documents:
        raise RuntimeError("No PDF documents found")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"Total chunks created: {len(chunks)}")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_STORE_DIR)

    print("Vector store saved successfully.")

if __name__ == "__main__":
    ingest_documents()

