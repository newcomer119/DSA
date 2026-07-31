
# Code
# Testcase
# Testcase
# Test Result
# 90. Subsets II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_index,path):
            ans.append(path[:])
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue 

                path.append(nums[i])
                dfs(i + 1,path)
                path.pop()
        ans = []
        nums.sort()
        dfs(0, [])
        return ans


        # def dfs(start_index, path):
        #     ans.append(path[:])
        #     for i in range(start_index, len(nums)):
        #         if i > start_index and nums[i] == nums[i - 1]:
        #             continue 

        #         path.append(nums[i])
        #         dfs(i + 1,path)
        #         path.pop()

        # ans = []
        # nums.sort()
        # dfs(0, [])
        # return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    got = sorted(map(tuple, sol.subsetsWithDup([1, 2, 2])))
    exp = sorted(map(tuple, [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] subsetsWithDup -> {len(got)} subsets")
    print(f"\n{1 if ok else 0}/1 passed")