def smallest_missing_three_sum(nums: list[int]) -> int:
    """
    Return the smallest positive integer that cannot be formed
    as the sum of exactly 3 distinct elements from nums.

    Distinct means different indices.
    """
    sums = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                ans = nums[i] + nums[j] + nums[k]
                sums.add(ans)

    missing = 1
    while missing in sums:
        missing += 1

    return missing


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([-2, -1, 1, 2, 3], 5),
    ([1, 2, 3], 1),
    ([-1, 0, 1, 2], 4),
    ([-2, 0, 1, 2, 3], 7),
    ([-3, -1, 1, 2, 4], 1),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, expected in test_cases:

    result = smallest_missing_three_sum(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)
