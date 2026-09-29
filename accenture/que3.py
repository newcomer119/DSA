def most_frequent_smallest(nums: list[int]) -> int:
    """
    Return the element that occurs most frequently.

    If multiple elements have the same highest frequency,
    return the SMALLEST element among them.
    """

    # Write your solution here
    freq ={}
    for num in nums:
        freq[num] = freq.get(num ,0) + 1
    max_count = 0
    ans = 0
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            ans = num
        elif count ==max_count and num < ans:
            ans = num
    return ans

# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([1, 2, 2, 3, 3, 3], 3),

    ([4, 4, 2, 2, 7], 2),

    ([5, 5, 5, 2, 2], 5),

    ([8, 1, 8, 1], 1),

    ([-1, -1, 2, 2, 3], -1),

    ([10], 10),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, expected in test_cases:
    result = most_frequent_smallest(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)