
# Architecture

This project follows a standard Retrieval-Augmented Generation (RAG) architecture optimized for simplicity, speed, and cost efficiency.

---

## Pipeline Overview

1. PDF documents are loaded from disk
2. Text is split into overlapping chunks
3. Each chunk is converted into a vector embedding
4. Embeddings are stored in a FAISS index
5. User queries retrieve top-k similar chunks
6. Retrieved context is passed to the LLM for answer generation

---

## Chunking Strategy

- Fixed-size text chunks
- Chunking balances:
  - Retrieval accuracy
  - Context window limits
  - Index size

Improper chunking leads to either:
- Loss of semantic meaning (too small)
- Poor retrieval precision (too large)

---

## Vector Store Choice: FAISS

FAISS was selected because:
- Fast local similarity search
- No external dependencies
- Ideal for small-to-medium document sets
- Easy to persist and reload indexes

This makes it suitable for local experimentation and production prototypes.

---

## Embedding Model

OpenAI embeddings are used for:
- High semantic accuracy
- Strong performance across technical and natural language text

All documents and queries share the same embedding space.

---

## LLM Choice: GPT-5-mini

GPT-5-mini is used because it provides:
- Low latency
- Very low cost per request
- Strong performance in RAG-style Q&A

The model is restricted to retrieved context only to avoid hallucinations.

---

## Limitations

- No metadata-based filtering
- Single-user, local execution
- No streaming responses
- No evaluation metrics yet

These are intentional trade-offs for clarity and learning.
