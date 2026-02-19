# Equity-Research-Tool
```
                ┌──────────────────────┐
                │   Financial Documents│
                │ (PDFs, Reports, News)│
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Document Loaders   │
                │  (LangChain Loaders) │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Text Splitter      │
                │ (Chunking + Overlap) │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Embedding Model    │
                │ (Semantic Vectors)   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Vector Database    │
                │ (FAISS / Chroma etc.)│
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ User Query  │ →  │  Retriever  │ →  │ Relevant    │
│ (Question)  │    │ (Top-K)     │    │ Chunks      │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
                                            ▼
                                ┌──────────────────────┐
                                │   LLM (LangChain)    │
                                │ (OpenAI / Groq)      │
                                └──────────┬───────────┘
                                           │
                                           ▼
                                ┌──────────────────────┐
                                │   Final Answer       │
                                │ (Grounded Response)  │
                                └──────────────────────┘
```



