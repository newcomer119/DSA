def subarray_sum(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum equals k.
    """

    # Write your solution here
    prefix = {0 : 1}
    curr_sum = 0
    count = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        complement = curr_sum - k
        for complement in prefix:
            count += prefix[complement]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

    return count



# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1, -1, 0], 0, 3),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ([1], 1, 1),
    ([1], 0, 0),
    ([0, 0, 0], 0, 6),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, k, expected in test_cases:
    result = subarray_sum(nums, k)

    print(f"nums     = {nums}")
    print(f"k        = {k}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)