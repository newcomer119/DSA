# Range Sum Query - Immutable
# Given an integer array nums, calculate the sum of elements between indices left and right (inclusive). You need to answer multiple queries efficiently. You are required to preprocess the array so that each query can be answered in constant time.

# Example: Input: nums = [1, 2, 3, 4], sumRange(1, 3). Output: 9.

# Your function should return 9 because the sum of elements from index 1 to 3 is 2 + 3 + 4 = 9.


from itertools import accumulate

def init_sum_array(nums: list[int]) -> list[int]:
    return list(accumulate(nums,initial = 0))

def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    cumm_sum  = init_sum_array(nums)
    return cumm_sum[right + 1] - cumm_sum[left]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 2, 3, 4], 1, 3, 9), ([1, 2, 3, 4], 0, 0, 1), ([5, 5, 5], 1, 2, 10)]
    passed = 0
    for nums, left, right, exp in TESTS:
        got = range_sum_query_immutable(nums, left, right)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] sum({left},{right})={got}")
    print(f"\n{passed}/{len(TESTS)} passed")