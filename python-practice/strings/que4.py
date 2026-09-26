def count_log_levels(logs: list[str]) -> dict[str, int]:
    freq = {}
    for log in logs:
        words = log.split(":")
        level = words[0]
        freq[level] = freq.get(level, 0) + 1
    return freq 

def run_tests():
    tests = [
        {
            "input": [
                "INFO: Server started",
                "ERROR: Database connection failed",
                "WARNING: Memory usage high",
                "ERROR: Request timeout",
                "INFO: User logged in"
            ],
            "expected": {
                "INFO": 2,
                "ERROR": 2,
                "WARNING": 1
            }
        },
        {
            "input": [
                "ERROR: Failed",
                "ERROR: Failed again",
                "ERROR: Still failed"
            ],
            "expected": {
                "ERROR": 3
            }
        },
        {
            "input": [
                "INFO: Started"
            ],
            "expected": {
                "INFO": 1
            }
        },
        {
            "input": [],
            "expected": {}
        }
    ]

    for i, test in enumerate(tests, 1):
        result = count_log_levels(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("Input:   ", test["input"])
            print("Expected:", test["expected"])
            print("Got:     ", result)


if __name__ == "__main__":
    run_tests()