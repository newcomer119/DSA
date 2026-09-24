def most_common_word(text: str) -> str:
    freq = {}
    text = text.lower()
    for char in ",.!?":
        text = text.replace(char, "")

    words = text.split()

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    max_count = 0
    answer = ""

    for word, count in freq.items():
        if count > max_count:
            max_count = count
            answer = word



    return answer



def run_tests():
    tests = [
        {
            "input": "Python is great, and python is easy. PYTHON!",
            "expected": "python"
        },
        {
            "input": "cat dog DOG cat bird",
            "expected": "cat"
        },
        {
            "input": "Hello, hello! HELLO?",
            "expected": "hello"
        },
        {
            "input": "apple banana apple banana orange",
            "expected": "apple"
        },
        {
            "input": "one two three three two two",
            "expected": "two"
        },
        {
            "input": "",
            "expected": ""
        },
        {
            "input": "   ",
            "expected": ""
        }
    ]

    for i, test in enumerate(tests, 1):
        result = most_common_word(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", repr(test["input"]))
            print("  Expected:", repr(test["expected"]))
            print("  Got:     ", repr(result))


if __name__ == "__main__":
    run_tests()