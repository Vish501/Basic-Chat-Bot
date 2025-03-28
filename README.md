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


## Setting Up the Google API Key

To use the Gemini API, you need to set up your GOOGLE_API_KEY:

1. Obtain your **Google API Key** from the **Google Cloud Console**.
2. Add the API key to your environment:
     - Locally (Linux/macOS): ```export GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - Command Prompt): ```set GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - PowerShell): ```$env:GOOGLE_API_KEY="your-api-key-here"```

3. If you are using GitHub Codespaces, store the API key as a GitHub repository secret:
     
     - Go to your GitHub repository
     - Navigate to **Settings > Secrets and variables > Actions**
     - Click **New repository secret**
     - Set the name as ```GOOGLE_API_KEY``` and paste your API key as the value
     - Click **Add secret**

This will allow the chatbot to authenticate and communicate with the Gemini API securely.

## Usage

1. Run the chatbot:

   ```bash
    streamlit run improved_simple_chatbot.py
  
2. Interact with the bot:

     Once the script is running, type your messages to the bot in the chat box provided. The bot will then respond based on the input provided.

## Files

- improved_simple_chatbot.py: Main script to run the chatbot with enhanced features.
- simple_chatbot.py: Initial version of the chatbot script.
- requirements.txt: List of Python packages required to run the chatbot.

## Acknowledgment

This project utilizes the Gemini API to power the chatbot's language understanding capabilities. For more information, visit the Hugging Face Space.
