def clean_scores(scores: list[int]) -> list[int]:
    res = []
    seen = set()

    for num in scores:
        if num < 0:
            continue
        if num in seen:
            continue 
        seen.add(num)
        num = num * 2
        res.append(num)

    return res

    


def run_tests():
    tests = [
        {
            "input": [5, -2, 3, 5, 7, -1, 3],
            "expected": [10, 6, 14]
        },
        {
            "input": [1, 2, 2, 3, 1],
            "expected": [2, 4, 6]
        },
        {
            "input": [-5, -2, -1],
            "expected": []
        },
        {
            "input": [0, 0, 5, 0, 10],
            "expected": [0, 10, 20]
        },
        {
            "input": [4, -1, 4, 2, -3, 2, 8],
            "expected": [8, 4, 16]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = clean_scores(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()