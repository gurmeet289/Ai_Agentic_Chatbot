# Ai_Agentic_Chatbot

# Intelligent LangGraph Agentic AI Agent

A modular AI chatbot framework using **LangGraph**, **FastAPI**, and **Streamlit**, built with clean OOP principles. This project allows you to define AI agent behaviors, choose LLM providers, and optionally enable real-time web search — all from a single, simple UI.

---

# Agentic AI Chatot Architecture Design Flow

![Agentic_AI_Chatbot_Flow](https://github.com/user-attachments/assets/1749a2d3-1a3c-4f45-a168-593dad8f306b)

# Agentic AI Chatot Demo Video




## 📁 Project Structure

    project/
    │
    ├── ai_agents/
    │ ├── init.py # Package initializer
    │ ├── config.py # Loads API keys & environment
    │ └── agent.py # LangGraph AI Agent class (OOP)
    │
    ├── api/
    │ ├── init.py
    │ └── backend.py # FastAPI backend server
    │
    ├── frontend/
    │ ├── init.py
    │ └── frontend.py # Streamlit UI
    │
    ├── main.py
    ├── .env # API keys
    └── requirements.txt # Python dependencies


---

## Features

- **Web UI** via Streamlit
- **FastAPI** backend with JSON API
- Modular **LangGraph AI agent**
- Optional **Web search tool** (Tavily)
- Clean, maintainable code using OOP

---

## Tech Stack

- Python 3.10+
- Langgraph
- FastAPI
- Streamlit
- Groq LLMs
- Tavily Search Tool

---

## Environment Setup

### 1. Clone the Repository

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

### 2. Create Virtual Environment

    conda create -p venv python==3.10 -y
    source venv/bin/activate 
    
### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Create a .env File

  # .env
    GROQ_API_KEY=your-groq-api-key
    TAVILY_API_KEY=your-tavily-api-key
 
## Running the Application
Use this command to start both the backend (FastAPI) and frontend (Streamlit) from one terminal:

    python main.py


## Access the App individually

    Frontend (Streamlit): http://localhost:8501
    
    Backend (FastAPI): http://127.0.0.1:9999/docs (Swagger UI)

## Supported Models

### Currently supported via Groq:

    llama-3.3-70b-versatile
    
    deepseek-r1-distill-llama-70b

## Thank You! Keep Learning!

