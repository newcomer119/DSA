# Flexible Size Sliding Window - Longest
# Recall finding the largest size k subarray sum of an integer array in Largest Subarray Sum. What if we don't need the largest sum among all subarrays of fixed size k, but instead, we want to find the length of the longest subarray with sum smaller than or equal to a target?

# Given an array of non-negative integers nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4.


def subarray_sum_longest(nums: list[int], target: int) -> int:
    wsum =0
    length = 0
    left =0 
    for right in range(len(nums)):
        wsum += nums[right]
        while wsum > target:
            wsum -= nums[left]
            left += 1
        length = max(length,right - left + 1)
    return length 
    


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 6, 3, 1, 2, 4, 5], 10, 4), ([1, 2, 3], 6, 3), ([1, 1, 1, 1], 3, 3)]
    passed = 0
    for nums, target, exp in TESTS:
        got = subarray_sum_longest(nums, target)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")