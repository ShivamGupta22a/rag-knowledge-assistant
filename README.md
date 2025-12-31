# RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) system that allows querying PDF documents using
FAISS vector search and OpenAI GPT-5-mini.

## Features
- PDF ingestion and chunking
- Vector indexing with FAISS
- Context-aware question answering
- OpenAI GPT-5-mini integration

## Setup

```bash
git clone <your-repo-url>
cd rag-knowledge-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
