import os
from dotenv import load_dotenv

from google import genai

load_dotenv("keys.env")
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print(f"defining API Key; {api_key}")

def main():
    print("Hello from ask-nicely!")

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    )

    print(f"Response: {response.text}")
    print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
    print(f"Response tokens: {usage_metadata.candidate_token_count}")

if __name__ == "__main__":
    main()
