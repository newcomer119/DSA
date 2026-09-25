def remove_target(nums: list[int], target: int) -> list[int]:
    res = []

    for num in nums:
        if num == target:
            continue
        res.append(num)

    return res

def run_tests():
    tests = [
        {
            "nums": [3, 5, 2, 5, 7, 5, 8],
            "target": 5,
            "expected": [3, 2, 7, 8]
        },
        {
            "nums": [1, 2, 3],
            "target": 10,
            "expected": [1, 2, 3]
        },
        {
            "nums": [4, 4, 4],
            "target": 4,
            "expected": []
        },
        {
            "nums": [],
            "target": 2,
            "expected": []
        },
        {
            "nums": [-1, 2, -1, 3],
            "target": -1,
            "expected": [2, 3]
        }
    ]

    for i, test in enumerate(tests, 1):
        result = remove_target(test["nums"], test["target"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["nums"])
            print("  Target:  ", test["target"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()