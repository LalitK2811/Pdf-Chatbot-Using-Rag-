# 📄 PDF Chatbot using RAG 🚀

An AI-powered PDF Question Answering system built using **Streamlit**, **LangChain**, **FAISS**, and **Groq LLM**.

This project allows users to upload PDF documents and ask questions directly from the uploaded files using **Retrieval-Augmented Generation (RAG)**.

The system extracts text from PDFs, converts the text into embeddings, stores them in a vector database, retrieves the most relevant information using semantic search, and generates accurate answers using a Large Language Model (LLM).

---

# 📌 Project Overview

This project demonstrates the practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embedding Models
- Large Language Models (LLMs)

The application follows a complete end-to-end AI workflow:

- PDF text extraction
- Text chunking
- Embedding generation
- Vector storage using FAISS
- Semantic similarity search
- Context-aware answer generation using Groq LLM

The main objective of this project is to build an intelligent document-based chatbot capable of understanding PDF content and answering user queries accurately.

---

# 🧠 Problem Statement

Reading large PDF documents manually can be difficult and time-consuming.

Traditional search systems rely on keyword matching and often fail to understand the actual meaning and context of user queries.

This project solves that problem by building an AI-powered chatbot that can:

- Understand uploaded PDF documents
- Retrieve relevant information intelligently
- Perform semantic search
- Generate context-aware answers in natural language

The system uses Retrieval-Augmented Generation (RAG) architecture to improve answer accuracy and reduce hallucinations.

---

# 📁 Project Structure

```bash
project-folder/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── screenshots/
│   └── app_preview.png
│
└── notebooks/
    └── rag_pipeline_explanation.ipynb
```

---

# 📊 Project Workflow

```text
PDF Upload
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Embedding Generation
     ↓
Store Embeddings in FAISS
     ↓
Similarity Search
     ↓
Relevant Context Retrieval
     ↓
Groq LLM
     ↓
Final Answer
```

---

# 📚 PDF Text Extraction

The application extracts text from uploaded PDF files using:

```python
PyPDF2
```

Each PDF is processed page-by-page and converted into raw textual content for further processing.

---

# ✂️ Text Chunking

Large PDF documents are divided into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

Chunking helps improve:

- semantic retrieval,
- context preservation,
- search efficiency,
- and answer quality.

---

# 🧠 Embedding Generation

The text chunks are converted into vector embeddings using:

```python
FastEmbedEmbeddings
```

Embeddings are numerical vector representations of text that help the system understand semantic meaning instead of exact keyword matching.

### Example

```text
"Artificial Intelligence"
```

and

```text
"AI"
```

will generate similar embeddings because they represent similar meanings.

---

# 🗂️ Vector Database (FAISS)

The generated embeddings are stored inside:

```python
FAISS
```

FAISS is used for:

- fast similarity search,
- semantic retrieval,
- efficient vector storage,
- and context-based document search.

When the user asks a question, FAISS retrieves the most relevant chunks from the uploaded PDFs based on vector similarity.

---

# 🔍 Semantic Search

Unlike traditional keyword search, semantic search understands the meaning and intent behind the query.

### Example

Question:

```text
What is deep learning?
```

Even if the PDF contains:

```text
Neural networks are advanced machine learning models
```

the system can still retrieve relevant information because embeddings capture semantic relationships between words.

---

# 🤖 LLM Response Generation

The retrieved context is passed to:

```python
llama-3.3-70b-versatile
```

through the Groq API.

The Large Language Model generates a detailed answer strictly based on the retrieved document context.

The prompt is designed to:

- provide structured answers,
- avoid hallucinations,
- generate context-aware responses,
- and improve answer quality.

---

# 🧩 Retrieval-Augmented Generation (RAG)

This project is built using the RAG architecture.

RAG combines:

| Component | Purpose |
|---|---|
| Retrieval | Retrieve relevant document chunks |
| Generation | Generate natural language answers |

### RAG Pipeline

```text
PDF → Embeddings → FAISS → Retrieval → LLM → Answer
```

This architecture improves factual accuracy by grounding the LLM response in retrieved document content.

---

# 🌐 Streamlit Web Application

The Streamlit interface allows users to:

- Upload multiple PDF documents
- Process documents dynamically
- Ask questions from uploaded files
- Get AI-generated detailed answers instantly

The application is designed with a clean and user-friendly interface for better usability.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | Web Application |
| LangChain | LLM Workflow |
| FAISS | Vector Database |
| FastEmbed | Embedding Generation |
| Groq API | Large Language Model |
| PyPDF2 | PDF Text Extraction |

---

# ⚙️ Installation

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the project directory:

```env
GROQ_API_KEY=your_api_key
```


# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📦 requirements.txt

```txt
streamlit
python-dotenv
PyPDF2
langchain
langchain-community
langchain-groq
faiss-cpu
fastembed
```

---

# 📈 Key Learnings

This project helped in understanding:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embedding Models
- LangChain Workflows
- FAISS Similarity Search
- Groq LLM Integration
- Real-world AI application development

---

# 🔮 Future Improvements

- Chat History
- OCR Support for Scanned PDFs
- Citation-Based Answers
- Multi-language Support
- PDF Summarization
- Memory-Based Conversations

---

# 👨‍💻 Author

## Lalit Kirange

Computer Engineering Student  
Data Science & Generative AI Enthusiast

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
