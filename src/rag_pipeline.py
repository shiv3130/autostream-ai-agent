import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_DB_PATH = "vector_store"

# Load embeddings once globally
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def build_vector_store():

    loader = TextLoader("data/knowledge_base.md")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local(VECTOR_DB_PATH)

    return vectorstore


def load_vector_store():

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve_docs(query):

    if not os.path.exists(VECTOR_DB_PATH):
        vectorstore = build_vector_store()
    else:
        vectorstore = load_vector_store()

    docs = vectorstore.similarity_search(query, k=5)

    return docs
