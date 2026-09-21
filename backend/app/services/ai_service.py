import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
#from google.genai.types import HttpOptions

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class AIService:

    def __init__(self):
        self.client = genai.Client(
            #vertexai=True,
            #project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            #location=os.getenv("GOOGLE_CLOUD_LOCATION"),
            api_key=os.getenv("GEMINI_API_KEY"),
            #http_options=HttpOptions(api_version="v1"),
        )

    def generate_test_cases(self, title: str, description: str):

        prompt = f"""
You are a senior QA engineer.

Generate software test cases for this requirement.

Requirement:
Title: {title}
Description: {description}

Include positive, negative, boundary, and security scenarios where appropriate.

Return ONLY valid JSON:

{{
  "test_cases": [
    {{
      "title": "string",
      "description": "string",
      "steps": "string",
      "expected_result": "string"
    }}
  ]
}}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,  
        )

        return {"model": "gemini-2.5-flash", "prompt": prompt, "response": response.content}