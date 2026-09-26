def word_frequency(text: str) -> dict[str, int]:
    freq = {}
    text = text.lower()
    for char in ".,!?":
        text = text.replace(char, " ")

    words = text.split()

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def run_tests():
    tests = [
        {
            "input": "Python is great, python is easy! Python.",
            "expected": {
                "python": 3,
                "is": 2,
                "great": 1,
                "easy": 1
            }
        },
        {
            "input": "Hello, HELLO! hello?",
            "expected": {
                "hello": 3
            }
        },
        {
            "input": "  cat   dog cat  ",
            "expected": {
                "cat": 2,
                "dog": 1
            }
        },
        {
            "input": "",
            "expected": {}
        },
        {
            "input": "one,two,one",
            "expected": {
                "one": 2,
                "two": 1
            }
        }
    ]

    for i, test in enumerate(tests, 1):
        result = word_frequency(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", repr(test["input"]))
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()
