
# Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(k):
            heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappop(heap)
                heappush(heap, nums[i])

        return heap[0]


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),
        ([7, 6, 5, 4, 3, 2, 1], 3, 5),
    ]
    passed = 0
    for nums, k, expected in TESTS:
        got = sol.findKthLargest(nums, k)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] k={k} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")
