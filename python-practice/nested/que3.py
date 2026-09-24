def rotate_right(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []

    for _ in range(k):
        last = nums.pop()
        nums.insert(0,last)

    return nums
        


def run_tests():
    tests = [
        {
            "nums": [10, 20, 30, 40, 50],
            "k": 2,
            "expected": [40, 50, 10, 20, 30]
        },
        {
            "nums": [1, 2, 3],
            "k": 1,
            "expected": [3, 1, 2]
        },
        {
            "nums": [1, 2, 3],
            "k": 3,
            "expected": [1, 2, 3]
        },
        {
            "nums": [1, 2, 3],
            "k": 4,
            "expected": [3, 1, 2]
        },
        {
            "nums": [5],
            "k": 100,
            "expected": [5]
        },
        {
            "nums": [],
            "k": 3,
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        result = rotate_right(test["nums"], test["k"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["nums"], "k =", test["k"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()