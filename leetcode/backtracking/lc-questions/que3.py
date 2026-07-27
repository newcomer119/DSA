# 526. Beautiful Arrangement
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.


# Example 1:

# Input: n = 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
# Example 2:

# Input: n = 1
# Output: 1


# Constraints:

# 1 <= n <= 15

from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)

        def findBeautiful(i):
            if i > n:
                return 1

            count = 0
            for num in range(1, n + 1):
                if (not visited[num]) and (i % num == 0 or num % i == 0):
                    visited[num] = True
                    count += findBeautiful(i+1)
                    visited[num] = False
            return count
        return findBeautiful(1)


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [(1, 1), (2, 2), (3, 3)]
    passed = 0
    for n, exp in TESTS:
        got = sol.countArrangement(n)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
