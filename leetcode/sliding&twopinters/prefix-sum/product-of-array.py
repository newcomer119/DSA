# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Input: [1, 2, 3, 4].

# Output: [24, 12, 8, 6].


def product_of_array_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    left = 1
    res = [1] * n
    for i in range(len(nums)):
        res[i] *= left 
        left *= nums[i]

    right = 1
    for i in reversed(range(len(nums))):
        res[i] *= right
        right *= nums[i]

    return res 
    # length = len(nums)
    # res = [1] * length
    # left = 1
    # for i in range(len(nums)):
    #     res[i] *= left
    #     left *= nums[i]

    # right = 1
    # for i in reversed(range(len(nums))):
    #     res[i] *= right
    #     right *= nums[i]
        
    # return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 2, 3, 4], [24, 12, 8, 6]), ([1, 1], [1, 1]), ([5], [1])]
    passed = 0
    for nums, exp in TESTS:
        got = product_of_array_except_self(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")