def flatten(nums: list[list[int]]) -> list[int]:
    res = []
    for num in nums:
        for i in range(len(num)):
            res.append(num[i])

    return res


def run_tests():
    tests = [
        {
            "input": [[1, 2, 3], [4, 5], [], [6, 7, 8]],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8]
        },
        {
            "input": [[1], [2], [3]],
            "expected": [1, 2, 3]
        },
        {
            "input": [[], [], []],
            "expected": []
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [[10, -2], [0, 5]],
            "expected": [10, -2, 0, 5]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = flatten(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()