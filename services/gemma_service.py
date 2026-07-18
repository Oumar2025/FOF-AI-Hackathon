import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GemmaService:
    
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    @staticmethod
    def ask(prompt):

        try:

            response = GemmaService.client.models.generate_content(
                model="models/gemma-4-31b-it",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"AI Error: {e}"