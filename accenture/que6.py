def second_largest(nums: list[int]) -> int:
    """
    Return the second largest DISTINCT element.

    Return -1 if there is no second distinct largest element.
    """

    # Write your solution here

    unique_nums = set(nums)
    if len(unique_nums) < 2:
        return -1
    sorted_nums = sorted(unique_nums)
    return sorted_nums[-2]


# ==========================================
# TEST CASES
# ==========================================
test_cases = [
    ([10, 5, 20, 8], 10),
    ([5, 5, 5], -1),
    ([10, 20, 20, 8], 10),
    ([3, 1, 2], 2),
    ([1, 2], 1),
    ([7], -1),
    ([-5, -2, -10], -5),
    ([4, 4, 3, 3], 3),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, expected in test_cases:
    result = second_largest(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)
