def best_period(profits: list[int]) -> int:
    n = len(profits)
    largest = profits[0]
    csum = 0
    for i in range(n):
        for j in range(i, n):
            csum = 0
            for k in range(i, j + 1):
                csum += profits[k]

                if csum > largest:
                    largest = csum

    return largest 
    


def run_tests():
    tests = [
        {
            "input": [4, -2, 3, -5, 6],
            "expected": 6
        },
        {
            "input": [2, -1, 3, 4, -5],
            "expected": 8
        },
        {
            "input": [-5, -2, -8],
            "expected": -2
        },
        {
            "input": [5],
            "expected": 5
        },
        {
            "input": [1, 2, 3, 4],
            "expected": 10
        },
        {
            "input": [-2, 5, -1, 4, -10, 7],
            "expected": 8
        }
    ]

    for i, test in enumerate(tests, 1):
        result = best_period(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()