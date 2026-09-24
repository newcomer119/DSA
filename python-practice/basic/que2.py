def count_words(words: list[str]) -> dict[str, int]:
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1

    return freq 


def run_tests():
    tests = [
        {
            "input": ["Python", "java", "python", "C++", "JAVA", "python"],
            "expected": {"python": 3, "java": 2, "c++": 1}
        },
        {
            "input": ["Apple", "APPLE", "apple"],
            "expected": {"apple": 3}
        },
        {
            "input": ["cat", "dog", "cat", "bird", "dog", "cat"],
            "expected": {"cat": 3, "dog": 2, "bird": 1}
        },
        {
            "input": [],
            "expected": {}
        },
        {
            "input": ["A", "b", "C", "a", "B", "c", "c"],
            "expected": {"a": 2, "b": 2, "c": 3}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = count_words(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()