def minimum_difference(nums: list[int]) -> int:
    """
    Return the minimum absolute difference
    between any two distinct elements.

    nums contains at least 2 elements.
    """

    # Write your solution here

    sorted_nums = sorted(nums)
    min_diff = float("inf")
    for i in range(len(sorted_nums) - 1):
        diff = abs(sorted_nums[i + 1] - sorted_nums[i])

        if diff < min_diff:
            min_diff = diff

    return min_diff


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([4, 2, 1, 3], 1),
    ([10, 3, 20, 8], 2),
    ([1, 10, 5, 20], 4),
    ([5, 5, 10], 0),
    ([-10, -3, -7], 3),
    ([100, 50], 50),
    ([-5, 5, 15, 16], 1),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, expected in test_cases:
    result = minimum_difference(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)
