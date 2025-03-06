###################
# Simple Chat Bot #
###################

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import streamlit as st
import os
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ.get("HF_ACCESS_TOKEN")
os.environ["GOOGLE_API_KEY"] = os.environ.get("GENAI_API_KEY")

# Function to load the Google AI model and get responses
class GetGoogleAI():
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
                        model="gemini-1.5-pro",
                        temperature=0,
                        max_retries=2,
                        )

    def get_response(self, question):
        return self.llm.predict(question)
    

def main():
    chatAI = GetGoogleAI()

    st.set_page_config(page_title="Simply Q&A ChatBot")
    st.header("LangChain ChatBot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    input = st.text_input("Input: ", key="input")

    if st.button("Ask Question"):
        st.write(chatAI.get_response(input))

if __name__ == "__main__":
    main()
