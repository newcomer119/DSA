def has_pair_with_sum(nums: list[int], target: int) -> bool:
    nums = sorted(nums)

    l, r = 0, len(nums) - 1

    while l < r:
        two_sum = nums[l] + nums[r]

        if two_sum == target:
            return True

        if two_sum < target:
            l += 1
        else:
            r -= 1

    return False       

# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([8, 1, 4, 6], 10, True),
    ([1, 3, 5, 8], 20, False),
    ([2, 7, 11, 15], 9, True),
    ([5, 5], 10, True),
    ([5], 10, False),
    ([-3, 1, 4, 7], 4, True),
    ([-5, -2, 3, 10], 8, True),
    ([1, 2, 3, 4], 8, False),
]


# ==========================================
# TEST RUNNER
# ==========================================

for nums, target, expected in test_cases:
    result = has_pair_with_sum(nums, target)

    print(f"nums     = {nums}")
    print(f"target   = {target}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)