
# Code
# Testcase
# Testcase
# Test Result
# 967. Numbers With Same Consecutive Differences
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

 

# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(start_index, num):
            if start_index == n:
                ans.append(num)
                return 

            cur_digit = num % 10
            if(cur_digit - k >= 0):
                dfs(start_index + 1, num * 10 + (cur_digit - k))
            if(cur_digit + k <= 9 and k != 0):
                dfs(start_index + 1, num * 10 + (cur_digit + k))
        ans = []
        for i in range(1,10):
            dfs(1 ,i)
        return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    got = sorted(sol.numsSameConsecDiff(2, 1))
    ok = len(got) == 16
    print(f"[{'PASS' if ok else 'FAIL'}] n=2,k=1 -> {len(got)} numbers")
    print(f"\n{1 if ok else 0}/1 passed")