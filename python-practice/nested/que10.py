def group_numbers(nums: list[int]) -> dict[str, list[int]]:
    res = {
    "positive": [],
    "negative": [],
    "zero": []
  }
    for num in nums:
        if num < 0:
            res["negative"].append(num)
        elif num > 0:
            res["positive"].append(num)
        else:
            res["zero"].append(num)
            
    return res 


def run_tests():
    tests = [
        {
            "input": [4, -2, 7, 0, -5, 3, 0],
            "expected": {
                "positive": [4, 7, 3],
                "negative": [-2, -5],
                "zero": [0, 0]
            }
        },
        {
            "input": [1, 2, 3],
            "expected": {
                "positive": [1, 2, 3],
                "negative": [],
                "zero": []
            }
        },
        {
            "input": [-1, -2, -3],
            "expected": {
                "positive": [],
                "negative": [-1, -2, -3],
                "zero": []
            }
        },
        {
            "input": [0, 0],
            "expected": {
                "positive": [],
                "negative": [],
                "zero": [0, 0]
            }
        },
        {
            "input": [],
            "expected": {
                "positive": [],
                "negative": [],
                "zero": []
            }
        }
    ]

    for i, test in enumerate(tests, 1):
        result = group_numbers(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()