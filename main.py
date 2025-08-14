import os
import sys
from dotenv import load_dotenv

from google import genai

load_dotenv("keys.env")
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main(sys_argv=sys.argv[1]):
    print("Hello from ask-nicely!")
    
    sys_argv = Quandry
    string_tosend = f"{Quandry}"
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', string_tosend='contents'
    )

    print(f"Response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
