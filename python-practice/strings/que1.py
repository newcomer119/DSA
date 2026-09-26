def normalize_text(text: str) -> str:
    text = text.lower()
    words = text.split()
    return " ".join(words)

def run_tests():
    tests = [
        {
            "input": "   Python   is   GREAT   ",
            "expected": "python is great"
        },
        {
            "input": "  Hello     World  ",
            "expected": "hello world"
        },
        {
            "input": "AI",
            "expected": "ai"
        },
        {
            "input": "   one  two    three ",
            "expected": "one two three"
        },
        {
            "input": "",
            "expected": ""
        },
        {
            "input": "      ",
            "expected": ""
        }
    ]

    for i, test in enumerate(tests, 1):
        result = normalize_text(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", repr(test["input"]))
            print("Expected:", repr(test["expected"]))
            print("Got:     ", repr(result))


if __name__ == "__main__":
    run_tests()