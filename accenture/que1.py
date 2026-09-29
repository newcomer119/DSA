def smallest_missing_pair_sum(nums: list[int]) -> int:
    sums = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1,n):
            ans = nums[i] + nums[j]
            sums.add(ans)

    missing = 1
    while missing in sums:
        missing += 1

    return missing 
# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    # nums, expected
    ([1, 2, 4, 7], 1),
    ([-1, 2, 3, 4], 4),
    ([0, 1, 2], 1),
    ([-2, 2, 3], 2),
    ([1, 1, 2], 1),
]


for nums, expected in test_cases:
    result = smallest_missing_pair_sum(nums)

    print(f"nums     = {nums}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 30)