import os
from dotenv import load_dotenv
import gradio as gr

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.vector_stores.chroma.base import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
import chromadb


# === Load .env Variables ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === LlamaIndex Settings ===
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
Settings.llm = OpenAI(model="gpt-4o")  # or "gpt-3.5-turbo"
Settings.embed_model = OpenAIEmbedding()

# === ChromaDB Setup ===
CHROMA_DIR = "chroma_db"

def get_index():
    # If Chroma collection exists, load from it
    if os.path.exists(CHROMA_DIR):
        print("✅ Loading index from ChromaDB...")
        chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
        vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("llama_docs"))
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        return load_index_from_storage(storage_context)
    
    # Else, create new index
    print("🆕 Creating new index from documents...")
    documents = SimpleDirectoryReader("documents").load_data()
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("llama_docs"))
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    return index

# === Query Function ===
index = get_index()
query_engine = index.as_query_engine(similarity_top_k=3)

def answer_query(question):
    if not question.strip():
        return "Please enter a valid question."
    response = query_engine.query(question)
    return str(response)

# === Gradio UI ===
iface = gr.Interface(
    fn=answer_query,
    inputs=gr.Textbox(label="Ask a question about your documents:"),
    outputs=gr.Textbox(label="Answer"),
    title="📚 Document QA with LlamaIndex + ChromaDB",
    description="This app uses LlamaIndex + ChromaDB to answer questions from your document knowledge base."
)

if __name__ == "__main__":
    iface.launch()
