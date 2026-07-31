# 40. Combination Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start_index,path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return 

            for i in range(start_index, len(candidates)):
                if remaining - candidates[i] < 0:
                    break
                elif i != start_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1,path,remaining - candidates[i])
                path.pop()

        candidates.sort()
        ans = []
        dfs(0,[],target)
        return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    got = sorted(map(tuple, sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))
    exp = sorted(map(tuple, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] combinationSum2 target=8 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")