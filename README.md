# Text Completion AI Application

This Python application interacts with the OpenAI GPT API to provide text completions based on user prompts. Users can input a text prompt, and the application will send it to the AI model and display the generated response. It also allows for adjusting parameters like temperature and max tokens for more fine-tuned outputs.

## Prerequisites

*   Python 3.7+
*   An OpenAI API Key

## Setup Instructions

1.  **Clone the Repository (or download the files):**
    If this were a Git repository, you would clone it. For now, ensure you have the project files (`text_completion_app.py`, `requirements.txt`) in a local directory.

2.  **Create and Activate a Virtual Environment (Recommended):**
    It's good practice to use a virtual environment for Python projects.
    ```bash
    # Create a virtual environment (e.g., named .venv)
    python -m venv .venv

    # Activate the virtual environment
    # On Windows (Git Bash or similar)
    source .venv/Scripts/activate
    # On Windows (Command Prompt/PowerShell)
    # .venv\Scripts\activate
    # On macOS/Linux
    # source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    With your virtual environment activated, install the required Python libraries using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Your API Key:**
    *   Create a file named `.env` in the root directory of the project (the same directory as `text_completion_app.py`).
    *   Open the `.env` file and add your OpenAI API key in the following format:
        ```env
        OPENAI_API_KEY='your_openai_api_key_here'
        ```
    *   Replace `'your_openai_api_key_here'` with your actual OpenAI API key.
    *   **Important:** The `.env` file is included in `.gitignore` and should never be committed to version control.

## Usage

1.  **Run the Application:**
    Navigate to the project directory in your terminal (ensure your virtual environment is activated if you created one) and run the script:
    ```bash
    python text_completion_app.py
    ```

2.  **Interact with the Application:**
    *   The application will greet you and prompt you to enter your text.
    *   After entering your prompt, you will be asked to provide:
        *   **Temperature** (0.0-2.0, default: 0.7): Controls the randomness of the output. Lower values are more deterministic, higher values are more creative. Press Enter to use the default.
        *   **Max Tokens** (e.g., 50, 150, default: 150): Sets the maximum length of the generated response. Press Enter to use the default.
    *   The AI's response will then be displayed.
    *   You can continue entering new prompts.

3.  **Exit the Application:**
    Type `quit` at the prompt and press Enter to close the application.

## Dependencies

The application relies on the following Python libraries:

*   `openai`: The official Python library for interacting with the OpenAI API.
*   `python-dotenv`: Used to load environment variables (like your API key) from a `.env` file.

These are listed in the `requirements.txt` file.

## Features

*   Interactive command-line interface.
*   Direct interaction with OpenAI's GPT models (configurable, defaults to `gpt-3.5-turbo`).
*   User-adjustable parameters for `temperature` and `max_tokens` per request.
*   Basic input validation for prompts and parameters.
*   Error handling for common API issues (e.g., connection errors, rate limits, invalid API key). 