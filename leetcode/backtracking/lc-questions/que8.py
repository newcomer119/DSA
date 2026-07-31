
# Code
# 47. Permutations II
# premium lock icon
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used  = [False]  *len(nums)
        ans = []
        nums.sort()

        def dfs(start_index, path):
            if start_index == len(nums):
                ans.append(path[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue 

                if (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue 

                path.append(nums[i])
                used[i] = True
                dfs(start_index + 1, path)
                used[i] = False
                path.pop()

        dfs(0, [])
        return ans

        # used = [False] * len(nums)
        # ans = []
        # nums.sort()
        # def dfs(start_index,path):
        #     if start_index == len(nums):
        #         ans.append(path[:])
        #         return 
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         if (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
        #             continue 
        #         path.append(nums[i])
        #         used[i] = True
        #         dfs(start_index + 1,path)
        #         used[i] = False
        #         path.pop()
        # dfs(0 , [])
        # return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    got = sorted(map(tuple, sol.permuteUnique([1, 1, 2])))
    exp = sorted(map(tuple, [[1, 1, 2], [1, 2, 1], [2, 1, 1]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] permuteUnique [1,1,2] -> {len(got)} permutations")
    print(f"\n{1 if ok else 0}/1 passed")
