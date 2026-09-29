def longest_balanced_subarray(nums: list[int]) -> int:
    prefix = {0: -1}
    curr_sum = 0
    longest = 0

    for i in range(len(nums)):

        if nums[i] == 0:
            curr_sum -= 1
        else:
            curr_sum += 1

        if curr_sum in prefix:
            length = i - prefix[curr_sum]
            longest = max(longest, length)
        else:
            prefix[curr_sum] = i

    return longest


# ==========================================
# TEST CASES
# ==========================================
test_cases = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 0, 1, 0, 1, 1], 6),
    ([1, 1, 1, 0, 0], 4),
    ([0, 0, 0], 0),
    ([1, 1, 1], 0),
    ([0, 1, 1, 0, 1, 1, 1, 0], 4),
    ([1, 0, 0, 1, 0, 1], 6),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, expected in test_cases:
    result = longest_balanced_subarray(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)
