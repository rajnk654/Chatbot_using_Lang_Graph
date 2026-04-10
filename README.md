# Chatbot_using_Lang_Graph
📄 Multi-Utility LangGraph PDF Chatbot

A Multi-Utility AI Chatbot built using LangGraph, Streamlit, and Gemini (Google Generative AI) that supports:

📄 PDF-based Question Answering (RAG)
🔎 Web Search
🧮 Calculator
📈 Stock Price Lookup
💬 Multi-Thread Chat Sessions
🗂 Persistent Chat History

This project demonstrates Retrieval-Augmented Generation (RAG), tool usage, and multi-session conversation management using LangGraph workflows.

🚀 Features
🤖 AI Chat Assistant
Powered by Gemini 2.5 Flash Lite
Supports multi-turn conversations
Maintains persistent chat history
📄 PDF Chat (RAG)
Upload PDF documents
Automatically:
Extracts text
Splits into chunks
Stores embeddings
Retrieves relevant context
Answers questions based on uploaded documents
🔎 Web Search Tool

Uses:

DuckDuckGo Search API

Allows:

Real-time information retrieval
Web-based answers
🧮 Calculator Tool

Supports:

Addition
Subtraction
Multiplication
Division

📈 Stock Price Tool

Fetches:

Real-time stock price
Uses Alpha Vantage API

Example:

Get stock price of AAPL

🧵 Multi-Thread Chat Sessions
Create new chat sessions
Switch between past conversations
Each thread stores:
Messages
Documents
Context
💾 Persistent Memory

Uses:

SQLite database
LangGraph Checkpointing

Chat sessions remain saved after restart.

🏗 Project Architecture
Multi-Utility Chatbot
│
├── langgraph_rag_frontend.py   # Streamlit UI
├── langgraph_rag_backend.py    # RAG + Tools Backend
├── langgraph_backend.py        # Basic Tool Chatbot
│
├── chatbot.db                  # SQLite Chat Memory
│
├── .env                        # API Keys
├── requirements.txt            # Dependencies
│
└── README.md

⚙️ Technologies Used
Category	Technology
Frontend	Streamlit
Backend	LangGraph
LLM	Gemini (Google Generative AI)
Embeddings	HuggingFace (MiniLM)
Vector Store	FAISS
Database	SQLite
Tools	DuckDuckGo, Calculator, Stock API
Language	Python

📦 Installation Guide
Step 1 — Clone Repository
git clone https://github.com/YOUR_USERNAME/langgraph-pdf-chatbot.git

cd langgraph-pdf-chatbot

Step 2 — Create Virtual Environment

Windows:

python -m venv .venv

.venv\Scripts\activate

Linux / Mac:

python -m venv .venv

source .venv/bin/activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Setup Environment Variables

Create .env file:

GOOGLE_API_KEY=your_gemini_api_key

Optional:

ALPHA_VANTAGE_API_KEY=your_stock_api_key

▶️ Running the Application

Run Streamlit frontend:

streamlit run langgraph_rag_frontend.py

Open browser:

http://localhost:8501

📄 How PDF Chat Works (RAG Flow)
User Uploads PDF
        │
        ▼
Text Extraction
(PyPDFLoader)

        ▼
Text Chunking
(Recursive Splitter)

        ▼
Embedding Generation
(HuggingFace MiniLM)

        ▼
Vector Storage
(FAISS)

        ▼
Retriever

        ▼
LLM + Context

        ▼
Answer

🔧 Available Tools
Tool	Description
🔎 Search Tool	Retrieves web results
🧮 Calculator	Performs math operations
📈 Stock Tool	Fetches stock price
📄 RAG Tool	Queries uploaded PDF

💬 Example Prompts
General Chat
Explain artificial intelligence
PDF Questions
Summarize this document
What are the key points in section 2?

Calculator
Add 10 and 25
Stock Price
Get stock price of TSLA
Web Search
Latest AI news today

🧵 Chat Thread Management

Features:

New Chat Button
Thread History Sidebar
Persistent Conversations
Per-thread Document Storage

Each thread maintains:

Thread ID
Messages
Uploaded Documents
Vector Store

🧠 System Workflow (LangGraph)
START
   │
   ▼
Chat Node
   │
   ├── If Tool Needed
   │        ▼
   │     Tool Node
   │        │
   │        ▼
   │     Chat Node
   │
   ▼
Response

📂 Database Storage

SQLite file:

chatbot.db

Stores:

Chat history
Thread state
Messages

📊 Performance Highlights
Fast document retrieval using FAISS
Multi-thread conversation handling
Efficient memory checkpointing
Real-time tool execution

🔐 Environment Variables

Required:

GOOGLE_API_KEY

Optional:

ALPHA_VANTAGE_API_KEY

Stored in:

.env

📈 Future Improvements
Add support for:
DOCX files
Multiple PDFs per thread
Chat export feature
Voice input
User authentication

🧑‍💻 Author

Raj Kolekar

MCA Graduate | Full Stack Developer

Skills:

Python
LangGraph
LangChain
Streamlit
React
Spring Boot

📜 License

This project is licensed under:

MIT License
