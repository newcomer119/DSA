# Fixed Size Sliding Window
# Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

# For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.


def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum

    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(window_sum,largest)
    return largest


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 2, 3, 7, 4, 1], 3, 14), ([1, 1, 1, 1], 2, 2), ([5], 1, 5)]
    passed = 0
    for nums, k, exp in TESTS:
        got = subarray_sum_fixed(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")