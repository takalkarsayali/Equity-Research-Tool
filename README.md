# 📊 Equity Research Tool (LLM-Powered Financial Analysis)

### LLM-Powered Financial Analysis using Retrieval-Augmented Generation (RAG)

An AI-powered Equity Research Assistant that analyzes company documents and financial disclosures using Large Language Models (LLMs) and Vector Search.

This tool enables users to input company URLs or documents and ask intelligent financial questions such as:

- What are the company’s key revenue drivers?
- What risks are mentioned in recent filings?
- What is the company’s growth outlook?
- Summarize the latest financial disclosures.

## 📝Overview
![img](https://github.com/user-attachments/assets/fd770f98-0596-4325-829c-a367b21b5f53)

## 🚀 Features

- 🔎 URL-based document ingestion  
- 📚 Intelligent document chunking  
- 🧠 Retrieval-Augmented Generation (RAG) pipeline  
- 📊 Financial Q&A powered by Groq LLM  
- 📁 Source citation for transparency  
- ⚡ Fast similarity search using FAISS  
- 🌐 Interactive UI built with Streamlit  

## 🏗️ Architecture Overview

```
        User Input (Company URLs / Documents)
                    ↓
        Document Loader (Unstructured)
                    ↓
                Text Splitter
                    ↓
           Embeddings Generation
                    ↓
            FAISS Vector Store
                    ↓
                Retriever
                    ↓
                LLM (Groq)
                    ↓
       Final Answer + Source Documents

```

## 🧱 Core Components
| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| LLM | Groq API |
| Embeddings | LangChain Embeddings |
| Vector Store | FAISS |
| Document Loader | Unstructured |
| Orchestration | LangChain |
|  |  |

## 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| LLM | Groq API |
| Framework | LangChain |
| Vector Database | FAISS (CPU) |
| Document Processing | Unstructured |
| Environment Management | python-dotenv |
|                        |               |

## 📦 Installation
#### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/Equity-Research-Tool.git
cd Equity-Research-Tool
```
#### 2️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
#### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
## 🔐 Environment Setup
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key_here

## ⚠️ Important:
Never commit .env

API keys should be stored securely

## ▶️ Run the Application
```
streamlit run main.py
```
Open in browser:
http://localhost:8501

## 💡 How It Works
User provides company URLs.

The system:

- Loads content
- Splits into chunks
- Converts chunks into embeddings
- Stores them in FAISS
- User asks financial questions.
- Retriever finds relevant chunks.
- LLM generates contextual answer.
- Source documents are displayed for transparency.

## 📊 Example Use Cases

- Investment research
- Financial due diligence
- Earnings call analysis
- Risk factor extraction
- Competitive benchmarking
- MBA / Finance student research

## 🔥 Key Learning Outcomes

This project demonstrates:

- RAG architecture implementation
- Vector database usage
- LLM integration via API
- Secure secret management
- Git history rewriting & security practices
- Production-ready ML application design

## 📁 Project Structure

Equity-Research-Tool
```
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env (local only, not committed)
```
## ⚠️ Notes

- FAISS vector stores are generated locally and not pushed to GitHub.
- API keys are managed securely using environment variables.
- Designed for educational and research purposes.

## 🚀 Future Improvements

- Multi-company comparison dashboard
- Financial ratio extraction
- PDF report export
- Caching for faster queries
- Deployment on Streamlit Cloud

Integration with real-time financial APIs

## 👩‍💻 Author

Built as part of an advanced LLM + RAG learning journey focused on financial AI applications.

## Process Flow

```
                ┌──────────────────────┐
                │   Financial Documents│
                │ (PDFs, Reports, News)│
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Document Loaders   │
                │  (LangChain Loaders) │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Text Splitter      │
                │ (Chunking + Overlap) │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Embedding Model    │
                │ (Semantic Vectors)   │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Vector Database    │
                │ (FAISS / Chroma etc.)│
                └──────────┬───────────┘
        ┌──────────────────┼──────────────────┐
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
                                           ▼
                                ┌──────────────────────┐
                                │   Final Answer       │
                                │ (Grounded Response)  │
                                └──────────────────────┘
```

