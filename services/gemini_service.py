import os

from google import genai
from dotenv import load_dotenv

load_dotenv()
print("===================================")
print("API KEY:", os.getenv("GOOGLE_API_KEY"))
print("===================================")

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class GeminiService:

    @staticmethod
    def ask(prompt):

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text