def process_readings(readings: list[list[int]]) -> list[int]:
    res = []
    seen = set()
    for i in range(len(readings)):
        for j in range(len(readings[i])):
            value = readings[i][j]
            if value < 0:
                continue 
            if value in seen:
                continue 
            seen.add(value)
            res.append(value * 3)
    return res


def run_tests():
    tests = [
        {
            "input": [
                [10, -1, 20, 10],
                [5, 5, -3, 15],
                [-2, 8, 20]
            ],
            "expected": [30, 60, 15, 45, 24]
        },
        {
            "input": [
                [1, 2, 3],
                [3, 4, 1],
                [5]
            ],
            "expected": [3, 6, 9, 12, 15]
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
                [0, 0],
                [0, 2],
                [2, 4]
            ],
            "expected": [0, 6, 12]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [
                [],
                [7, -1, 7],
                []
            ],
            "expected": [21]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = process_readings(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()