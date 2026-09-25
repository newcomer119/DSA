def process_batches(batches: list[list[int]]) -> list[int]:
    res = []
    seen = set()
    for batch in batches:
        for num in batch:
            if num < 0:
                continue 
            if num in seen:
                continue 
            seen.add(num)
            if num % 2 == 0:
                num = num * 2
            else:
                num = num * 3

            res.append(num)
    return res


def run_tests():
    tests = [
        {
            "input": [
                [3, -1, 5, 3],
                [8, 5, -2],
                [10, 8, 4]
            ],
            "expected": [9, 15, 16, 20, 8]
        },
        {
            "input": [
                [1, 2, 3],
                [2, 4, 1]
            ],
            "expected": [3, 4, 9, 8]
        },
        {
            "input": [
                [-1, -2],
                [-3]
            ],
            "expected": []
        },
        {
            "input": [
                [0, 1, 0],
                [2, 1]
            ],
            "expected": [0, 3, 4]
        },
        {
            "input": [],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = process_batches(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()
