# 🧠 Chat Agent with LlamaIndex

A powerful **AI-powered conversational agent** using [LlamaIndex](https://github.com/jerryjliu/llama_index), [LangChain](https://github.com/langchain-ai/langchain), [ChromaDB](https://www.trychroma.com/), and [Gradio](https://gradio.app/) for document-based QA, contextual chat, and knowledge retrieval.

This project demonstrates how to build an **RAG (Retrieval-Augmented Generation)** system using your own documents.

---

## ✨ Features

* ✅ Document upload and indexing via LlamaIndex
* 🧠 Semantic search over your knowledge base
* 📂 ChromaDB for fast vector storage and retrieval
* 💬 OpenAI LLM for answering user queries with context
* 🧪 Gradio-based interactive UI
* 🔐 Secure API key handling using `.env`

---

## 📁 Project Structure

```
Chat_Agent_LlamaIndex/
│
├── docs/                          # Directory to hold uploaded documents
│
├── app.py                         # FastAPI app (can be expanded for API access)
├── ui.py                          # Gradio app for chat interface
├── index_utils.py                 # LlamaIndex functions: load, build, query index
├── prompt_helper.py               # Prompt tuning and configuration
│
├── .env                           # API key config
├── requirements.txt               # All dependencies
└── README.md                      # You are here!
```

---

## 🧪 Tech Stack

| Tool           | Role                               |
| -------------- | ---------------------------------- |
| **LlamaIndex** | Converts documents to vector index |
| **ChromaDB**   | Vector database for fast retrieval |
| **LangChain**  | Language model orchestration       |
| **OpenAI**     | LLM provider (e.g., GPT-4)         |
| **Gradio**     | Frontend chat UI                   |
| **FastAPI**    | Backend setup for API integration  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/javaidiqbal11/Chat_Agent_LlamaIndex.git
cd Chat_Agent_LlamaIndex
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI Key

Create a `.env` file in the root folder and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🚀 Running the App

### Start Gradio App

```bash
python ui.py
```

* The app will launch in your browser.
* Upload `.pdf`, `.docx`, or `.txt` files to populate the knowledge base.
* Ask questions in natural language based on the uploaded documents.

> You can modify Gradio port and config in `ui.py`.

---

## 🔍 How It Works

1. **Document Upload:**

   * Uploaded files are parsed and chunked.
   * Text is embedded using OpenAI embeddings.

2. **Index Creation:**

   * `LlamaIndex` builds a vector index over the text chunks.
   * Index is stored in ChromaDB for efficient vector search.

3. **Query Handling:**

   * User query is embedded and matched to relevant chunks.
   * A prompt is constructed and passed to OpenAI's GPT model.
   * Final answer is returned in a chat format.

---

## 🛠️ Core Components

### `index_utils.py`

* `build_index(doc_folder)` → builds index from documents
* `load_index()` → loads saved index from disk
* `query_index(index, query)` → gets response to user query

### `prompt_helper.py`

Customizes:

* Prompt length
* Chunk overlap
* Maximum input/output tokens

You can modify these for fine-tuning performance and cost.

---

## 📂 Document Support

Supports:

* `.pdf`
* `.docx`
* `.txt`

You can easily extend support in `index_utils.py`.

---

## 🧪 Sample Query Flow

```text
> Upload: telecom_policy.pdf

> Query: What are the charges for international roaming?

> Output: According to section 3 of telecom_policy.pdf, international roaming charges are...
```

---

## 🧱 Built With

* [LlamaIndex](https://github.com/jerryjliu/llama_index)
* [LangChain](https://github.com/langchain-ai/langchain)
* [ChromaDB](https://www.trychroma.com/)
* [OpenAI GPT-4](https://platform.openai.com/)
* [Gradio](https://www.gradio.app/)
* [FastAPI](https://fastapi.tiangolo.com/)

---

## 📌 Future Enhancements (Suggestions)

* ✅ Add MongoDB/FAISS as optional storage backends
* ✅ Support chat history (memory)
* ✅ Deploy on HuggingFace Spaces or AWS
* ✅ Add authentication layer for document upload
* ✅ Add LangSmith tracing/debugging

---

## 📜 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

## 🤝 Contribution

PRs and feedback are welcome! Open an issue or fork the repo to start contributing.

