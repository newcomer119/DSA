def character_frequency(text: str) -> dict[str, int]:
    freq = {}
    text = text.lower()
    for char in text:
        if char == " ":
            continue
        freq[char] = freq.get(char, 0) + 1

    return freq    


def run_tests():
    tests = [
        {
            "input": "banana",
            "expected": {"b": 1, "a": 3, "n": 2}
        },
        {
            "input": "Hello World",
            "expected": {
                "h": 1,
                "e": 1,
                "l": 3,
                "o": 2,
                "w": 1,
                "r": 1,
                "d": 1
            }
        },
        {
            "input": "AAAaaa",
            "expected": {"a": 6}
        },
        {
            "input": "a b a c",
            "expected": {"a": 2, "b": 1, "c": 1}
        },
        {
            "input": "",
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = character_frequency(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", repr(test["input"]))
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()