# Basic Chat Bot powered by Gemini.

## Overview

This project implements a simple AI chatbot using the Gemini API, enabling users to interact with the bot through natural language conversations. The chatbot leverages the Gemini language model to generate human-like responses.

## Features

- **Natural Language Understanding**: Utilizes the Gemini API to comprehend and process user inputs.
- **Conversational AI**: Engages in interactive dialogues, providing relevant and coherent responses.
- **Extensible Design**: Structured to allow easy integration of additional functionalities.

## Requirements

- Python 3.11.2
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:

     ```bash
     git clone https://github.com/Vish501/Basic-Chat-Bot.git
     cd Basic-Chat-Bot
    ```
     
2. **Install dependencies**:

    It's recommended to use a virtual environment to manage dependencies. You can create and activate one using:
   
     ```bash
     conda create -n venv python=3.11.2
    ```
     
     ```bash
    conda activate venv/
   ```
     Then, install the required packages: ```pip install -r requirements.txt```
    
## Usage

Run the chatbot:

   ```bash
    streamlit run improved_simple_chatbot.py
  ```

Interact with the bot:

    Once the script is running, type your messages to the bot in the chat box provided. The bot will then respond based on the input provided.

## Files

- improved_simple_chatbot.py: Main script to run the chatbot with enhanced features.
- simple_chatbot.py: Initial version of the chatbot script.
- requirements.txt: List of Python packages required to run the chatbot.

## Acknowledgments

This project utilizes the Gemini API to power the chatbot's language understanding capabilities. For more information, visit the Hugging Face Space.
