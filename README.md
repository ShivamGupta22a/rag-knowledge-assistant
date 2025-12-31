# RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) system for querying PDF documents using FAISS vector search and OpenAI GPT-5-mini.

This project demonstrates a complete, end-to-end RAG pipeline:
PDF ingestion → chunking → vector indexing → retrieval → context-aware Q&A.

---

## Features

- PDF ingestion with automatic text chunking
- OpenAI embeddings for semantic search
- Fast similarity search using FAISS
- Context-aware question answering
- GPT-5-mini for low-cost, fast inference
- Simple CLI-based interface

---

## Project Structure

```text
rag-knowledge-assistant/
├── app/
│   ├── ingest.py
│   ├── rag.py
│   ├── test_rag.py
│   └── main.py
├── data/sample_docs/
├── vector_store/
├── README.md
├── ARCHITECTURE.md
├── USAGE.md
├── ROADMAP.md
└── requirements.txt
```

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Advanced Usage](USAGE.md)
- [Roadmap](ROADMAP.md)

