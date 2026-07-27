# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1] Output: 0

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    size = len(nums)+1
    total, l = 0, 0
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:       # valid
            size = min(size, r-l+1)
            total -= nums[l]
            l += 1
    return size if size != len(nums)+1 else 0
# The above solution using a flexible sliding window uses O(n) time complexity. As a follow up, is there an algorithm that solves this question in O(n log(n))? Yes! Consider using the n elements in nums as a starting point of a subarray, and then use O(log(n)) time complexity to find the endpoint of that subarray. This is can be done via a for loop and a binary search on a prefix sum array.

def minSubArrayLen(target: int, nums: List[int]) -> int:
    prefix_sum = [0]
    for n in nums:
        prefix_sum.append(prefix_sum[-1] + n)

    size = len(nums)+1
    for start in range(len(nums)):
        total = 0
        l, r, end = 0, len(nums)-1, -1
        while l <= r:
            mid = (l+r)//2
            if prefix_sum[mid+1] - prefix_sum[start] >= target:
                end, r = mid, mid - 1
            else: l = mid + 1
        if end != -1: size = min(size, end-start+1)
    return size if size != len(nums)+1 else 0


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)]
    passed = 0
    for target, nums, exp in TESTS:
        got = minSubArrayLen(target, nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")