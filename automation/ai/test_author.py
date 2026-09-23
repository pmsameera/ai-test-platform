import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


ENV_FILE = Path(__file__).resolve().parents[3] / "backend" / "app" / ".env"
load_dotenv(ENV_FILE)


class AITestAuthor:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_test(self, requirement_file: Path, output_file: Path):
        requirement = requirement_file.read_text()

        prompt = f"""
You are a senior SDET.

Generate a complete executable Playwright Python test module
from the following requirement.

Requirement:
{requirement}

Rules:
- Use pytest.
- Use Playwright Python sync API.
- Generate actual executable Python code.
- Cover the acceptance criteria.
- Use semantic Playwright locators where possible.
- Do not return Markdown.
- Do not return explanations.
- Return ONLY the Python source code.
"""

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        code = response.text.strip()

        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(code)

        return output_file