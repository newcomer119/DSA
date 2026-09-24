def find_mismatches(expected: list[int], actual: list[int]) -> list[int]:
    res = []
    for i in range(len(expected)):
            if expected[i] != actual[i]:
                res.append(i)

    return res 
def run_tests():
    tests = [
        {
            "expected": [10, 20, 30, 40],
            "actual": [10, 25, 30, 50],
            "answer": [1, 3]
        },
        {
            "expected": [1, 2, 3],
            "actual": [1, 2, 3],
            "answer": []
        },
        {
            "expected": [5, 5, 5],
            "actual": [1, 5, 2],
            "answer": [0, 2]
        },
        {
            "expected": [],
            "actual": [],
            "answer": []
        },
        {
            "expected": [7],
            "actual": [8],
            "answer": [0]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = find_mismatches(
            test["expected"],
            test["actual"]
        )

        if result == test["answer"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Expected list:", test["expected"])
            print("  Actual list:  ", test["actual"])
            print("  Expected ans: ", test["answer"])
            print("  Got:          ", result)


if __name__ == "__main__":
    run_tests()