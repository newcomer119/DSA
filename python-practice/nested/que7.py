def calculate_changes(original: list[int], updated: list[int]) -> list[int]:
    res = []
    for i in range(len(original)):
        res.append(updated[i]- original[i])

    return res 


def run_tests():
    tests = [
        {
            "original": [10, 20, 30, 40],
            "updated": [13, 18, 30, 50],
            "expected": [3, -2, 0, 10]
        },
        {
            "original": [1, 2, 3],
            "updated": [1, 2, 3],
            "expected": [0, 0, 0]
        },
        {
            "original": [5, 10, 15],
            "updated": [3, 20, 10],
            "expected": [-2, 10, -5]
        },
        {
            "original": [-5, -2, 0],
            "updated": [-2, -5, 10],
            "expected": [3, -3, 10]
        },
        {
            "original": [],
            "updated": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = calculate_changes(
            test["original"],
            test["updated"]
        )

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Original:", test["original"])
            print("  Updated: ", test["updated"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()