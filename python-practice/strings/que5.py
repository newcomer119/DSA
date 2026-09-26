def extract_numbers(values: list[str]) -> list[int]:
    res = []
    for value in values:
        if not value.isdigit():
            continue 

        number = int(value)
        res.append(number)

    return res


def run_tests():
    tests = [
        {
            "input": ["10", "hello", "25", "-3", "7x", "42"],
            "expected": [10, 25, 42]
        },
        {
            "input": ["1", "2", "3"],
            "expected": [1, 2, 3]
        },
        {
            "input": ["hello", "abc", "-5"],
            "expected": []
        },
        {
            "input": ["0", "001", "50"],
            "expected": [0, 1, 50]
        },
        {
            "input": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = extract_numbers(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", test["input"])
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()