
# Code
# Testcase
# Testcase
# Test Result
# 473. Matchsticks to Square
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
 

# Constraints:

# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 108

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: return False
        side_length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        def dfs(start_index):
            if start_index == len(matchsticks):
                return side_length == sides[0] == sides[1] == sides[2] == sides[3]

            for i in range(4):
                if sides[i] + matchsticks[start_index] <= side_length:
                    sides[i] += matchsticks[start_index]
                    if dfs(start_index + 1): return True
                    sides[i] -= matchsticks[start_index]
            return False
        return dfs(0)


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [([1, 1, 2, 2, 2], True), ([3, 3, 3, 3, 4], False)]
    passed = 0
    for sticks, exp in TESTS:
        got = sol.makesquare(sticks)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {sticks} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")