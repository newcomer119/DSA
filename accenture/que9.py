def longest_subarray_at_most_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum is <= k.

    nums contains positive integers.
    """

    # Write your solution here
    longest= 0 
    left =0 
    window = 0
    for right in range(len(nums)):
        window += nums[right]
        while window >  k:
            window -= nums[left]
            left += 1
        longest = max(longest, right - left + 1)
    return longest 


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([2, 1, 3, 2, 1], 5, 2),
    ([1, 1, 1, 1], 3, 3),
    ([5, 1, 2, 1], 5, 3),
    ([1, 2, 3, 4, 5], 15, 5),
    ([4, 4, 4], 3, 0),
    ([2, 2, 2], 4, 2),
    ([1], 1, 1),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, k, expected in test_cases:
    result = longest_subarray_at_most_k(nums, k)

    print(f"nums     = {nums}")
    print(f"k        = {k}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)