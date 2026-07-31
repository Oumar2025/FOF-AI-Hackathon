import os

from google import genai
from dotenv import load_dotenv

load_dotenv()


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