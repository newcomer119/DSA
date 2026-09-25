def most_frequent(nums: list[int]) -> int:
    ans = 0
    maxcount = 0
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num,count in freq.items():
        if count > maxcount:
            maxcount = count
            ans = num

    return ans 
    




def run_tests():
    tests = [
        {
            "input": [4, 2, 4, 3, 2, 4, 5],
            "expected": 4
        },
        {
            "input": [5, 2, 5, 2, 3],
            "expected": 5
        },
        {
            "input": [1, 1, 2, 2, 3, 3],
            "expected": 1
        },
        {
            "input": [-1, -2, -1, -3, -1],
            "expected": -1
        },
        {
            "input": [7],
            "expected": 7
        }
    ]

    for i, test in enumerate(tests, 1):
        result = most_frequent(test["input"])

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print("  Input:   ", test["input"])
            print("  Expected:", test["expected"])
            print("  Got:     ", result)


if __name__ == "__main__":
    run_tests()