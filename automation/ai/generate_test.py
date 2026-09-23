from pathlib import Path

from test_author import AITestAuthor

requirement_file = Path("automation/requirements/REQ-001-login.md")
output_file = Path("automation/generated_tests/test_req_001_login.py")

author = AITestAuthor()

generated_file = author.generate_test(
    requirement_file,
    output_file,
)

print(f"Generated: {generated_file}")