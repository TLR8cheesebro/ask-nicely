import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv("keys.env")
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

def main():
    print("Hello from ask-nicely! your terminal prompt is being sent to Gemini-2, you silly, sexy thing ;)")
    
    if len(sys.argv) < 2:
        print("You forgot to enter a prompt! Please try again.")
        sys.exit(1)

# this is where we prep the prompt as a string
    sys_argv = sys.argv[1]  
    Quandry = ""
    Quandry = sys_argv
    string_tosend = f"{Quandry}"

# this is where I build an if statement to check if the prompt is empty
    if len(string_tosend) < 1:
        print("You didnt type any characters! Please try again.")
        sys.exit(1)
    else:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )

    print(f"User prompt: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
