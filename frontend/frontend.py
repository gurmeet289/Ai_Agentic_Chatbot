from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()


#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
st.set_page_config(page_title="Intelligent LangGraph Agentic AI Agent", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Please define the role for your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "deepseek-r1-distill-llama-70b"]

provider=st.radio("Your Provider:", ("Groq"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Do you want to allow web search?")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            try:
                response_data = response.json()  # Try to parse JSON
            except ValueError:
                # Fallback if backend sends plain string
                response_data = {"error": response.text}

            if isinstance(response_data, dict) and "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
        else:
            st.error(f"Request failed with status code {response.status_code}")




