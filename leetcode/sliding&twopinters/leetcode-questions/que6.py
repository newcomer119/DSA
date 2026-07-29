# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
# Question

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                l, r = l + 1, r-1
                while l < len(nums) - 1 and nums[l] == nums[l-1]:
                    l += 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return res

    # nums.sort()
    # res = []
    # for i in range(len(nums)):
    #     if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]: continue
    #     l, r = i+1, len(nums)-1
    #     while l < r:
    #         total = nums[i] + nums[l] + nums[r]
    #         if total == 0:
    #             res.append([nums[i], nums[l], nums[r]])
    #             l, r = l+1, r-1
    #             while l < len(nums) -1 and nums[l] == nums[l-1]:
    #                 l += 1
    #         elif total > 0:
    #             r -= 1
    #         else:
    #             l += 1
    # return res
# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    def norm(g): return sorted(sorted(x) for x in g)
    passed = 0
    for nums, exp in TESTS:
        got = norm(threeSum(nums[:]))
        ok = got == norm(exp)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
