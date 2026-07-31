# 89. Gray Code
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

 

# Example 1:

# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# Example 2:

# Input: n = 1
# Output: [0,1]
 

# Constraints:

# 1 <= n <= 16

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        length  =  1 << n
        visited = [False] * length

        def dfs(start_index, code):
            if start_index == length:
                return True 

            for i in range(n):
                new_code = code ^ (1 << i)
                if not visited[new_code]:
                    path.append(new_code)
                    visited[new_code] = True
                    if dfs(start_index + 1, new_code):
                        return True
                    visited[new_code] = False
                    path.pop()
            return False

        path = [0]
        visited[0] = True
        dfs(1, 0)
        return path

        # length = 1 << n   # same as 2**n
        # visited = [False] * length

        # def dfs(start_index, code):
        #     if start_index == length:
        #         return True
        #     for i in range(n):
        #         new_code = code ^ (1 << i)
        #         if not visited[new_code]:
        #             path.append(new_code)
        #             visited[new_code] = True
        #             if dfs(start_index+1, new_code): return True
        #             visited[new_code] = False
        #             path.pop()
        #     return False

        # path = [0]
        # visited[0] = True
        # dfs(1, 0)
        # return path


# --- Daily tests ---
if __name__ == "__main__":
    def valid_gray(seq, n):
        if len(seq) != 1 << n or len(set(seq)) != 1 << n or seq[0] != 0:
            return False
        diff1 = lambda a, b: (a ^ b).bit_count() == 1
        return all(diff1(seq[i], seq[i + 1]) for i in range(len(seq) - 1)) and diff1(seq[0], seq[-1])

    sol = Solution()
    passed = 0
    for n in [1, 2]:
        ok = valid_gray(sol.grayCode(n), n)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] grayCode n={n}")
    print(f"\n{passed}/2 passed")