from pathlib import Path


class TestHealer:

    def analyze_failure(self, test_file: Path, output: str):
        test_source = test_file.read_text()

        print("=== Healing Context ===")
        print(f"Test file: {test_file}")

        print("\n=== Failure Output ===")
        print(output)

        healed_source = test_source.replace(
            'name="WrongLogin"',
            'name="Login"',
        )

        healed_file = test_file.with_name(
            f"{test_file.stem}_healed.py"
        )

        healed_file.write_text(healed_source)

        print("\n=== Proposed Healing ===")
        print(f"Healed file: {healed_file}")

        return healed_file