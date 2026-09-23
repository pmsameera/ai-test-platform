import subprocess
import sys
from pathlib import Path

from healing.test_healer import TestHealer


AUTOMATION_DIR = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = AUTOMATION_DIR / "artifacts"
SCREENSHOT_DIR.mkdir(exist_ok=True)


def run_tests():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-v",
            "generated_tests",
        ],
        cwd=AUTOMATION_DIR,
        capture_output=True,
        text=True,
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    print(f"Test execution completed with exit code: {result.returncode}")

    if result.returncode != 0:
        screenshot_path = SCREENSHOT_DIR / "failure.png"

        healer = TestHealer()

        healer.analyze_failure(
            test_file=AUTOMATION_DIR / "generated_tests" / "test_req001_login.py",
            output=result.stdout + result.stderr,
            screenshot_path=screenshot_path,
        )

    return result.returncode


if __name__ == "__main__":
    run_tests()