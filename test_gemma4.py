import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="models/gemma-4-31b-it",
    contents="Say hello in one sentence."
)

print(response.text)