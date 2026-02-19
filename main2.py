import os
import streamlit as st
import pickle
import time

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# ---------------- UI ----------------
st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store.pkl"
main_placeholder = st.empty()


# ---------------- LLM (Groq) ----------------
llm = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0.3,
    groq_api_key=os.environ["GROQ_API_KEY"]
)


# ---------------- URL Processing ----------------
if process_url_clicked:
    # Load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading... Started ✅")
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ","],
        chunk_size=1000,
        chunk_overlap=200
    )
    main_placeholder.text("Text Splitting... Started ✅")
    docs = text_splitter.split_documents(data)

    # Embeddings (local, free)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Vector Store Created ✅")
    time.sleep(1)

    # Save FAISS index
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)


# ---------------- Question Answering ----------------
query = main_placeholder.text_input("Question:")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )

        result = qa_chain.invoke({"query": query})

        st.header("Answer")
        st.write(result["result"])

        st.subheader("Sources")
        for doc in result["source_documents"]:
            st.write(doc.metadata.get("source", "Unknown"))
