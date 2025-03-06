############################
# Improved Simple Chat Bot #
############################

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import streamlit as st
import os
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

load_dotenv()
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
    
# Main function, only run when file is directly called
def main():
    # Initialing Google AI
    chatAI = GetGoogleAI()

    st.set_page_config(page_title="Simply Q&A ChatBot")
    st.header("LangChain ChatBot")

    # Creating a session state to store messages so they persist during run time
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # If there are messages, display them with appropirate roles
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat box for message input from the user
    if input := st.chat_input("Ask Question"):
        st.session_state.messages.append({"role": "user", "content": input})
        # Show user's input
        with st.chat_message("user"):
            st.markdown(input)
        
        # Get response from AI
        ai_response = chatAI.get_response(input)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        # Show assistant's input
        with st.chat_message("assistant"):
            st.markdown(ai_response)        


if __name__ == "__main__":
    main()
