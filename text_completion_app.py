import openai
import os
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file or environment variables.")
    return api_key

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    try:
        openai.api_key = get_api_key()
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except openai.APIConnectionError as e:
        return f"API Connection Error: {e}"
    except openai.RateLimitError as e:
        return f"Rate Limit Exceeded: {e}"
    except openai.APIStatusError as e:
        return f"API Status Error: {e.status_code} - {e.response}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    print("Welcome to the Text Completion App!")
    print("Enter 'quit' at any time to exit.")

    default_temperature = 0.7
    default_max_tokens = 150

    while True:
        user_prompt = input("\nEnter your prompt: ")
        if user_prompt.lower() == 'quit':
            print("Exiting application. Goodbye!")
            break
        
        if not user_prompt.strip():
            print("Input cannot be empty. Please enter a prompt.")
            continue

        try:
            temp_input = input(f"Enter temperature (0.0-2.0, default: {default_temperature}): ")
            temperature = float(temp_input) if temp_input else default_temperature
            if not (0.0 <= temperature <= 2.0):
                print("Invalid temperature. Using default.")
                temperature = default_temperature
        except ValueError:
            print("Invalid input for temperature. Using default.")
            temperature = default_temperature

        try:
            mt_input = input(f"Enter max tokens (e.g., 50, 150, default: {default_max_tokens}): ")
            max_tokens = int(mt_input) if mt_input else default_max_tokens
            if max_tokens <= 0:
                print("Max tokens must be positive. Using default.")
                max_tokens = default_max_tokens
        except ValueError:
            print("Invalid input for max tokens. Using default.")
            max_tokens = default_max_tokens

        completion = get_completion(user_prompt, temperature=temperature, max_tokens=max_tokens)
        print("\nAI Response:")
        print(completion)

if __name__ == "__main__":
    main() 