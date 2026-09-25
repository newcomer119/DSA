def find_max_with_index(scores: list[int]) -> tuple[int, int]:
    max =float("-inf")
    largest_index = 0
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            largest_index = i

    return (max,largest_index)


def run_tests():
    tests = [
        {
            "input": [45, 82, 67, 91, 73],
            "expected": (91, 3)
        },
        {
            "input": [10, 50, 20, 50, 30],
            "expected": (50, 1)
        },
        {
            "input": [-10, -3, -20, -5],
            "expected": (-3, 1)
        },
        {
            "input": [7],
            "expected": (7, 0)
        },
        {
            "input": [100, 90, 80],
            "expected": (100, 0)
        }
    ]

    for i, test in enumerate(tests, 1):
        result = find_max_with_index(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()