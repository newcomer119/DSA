
# Code
# Testcase
# Testcase
# Test Result
# 1615. Maximal Network Rank
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 

# Example 1:



# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
# Example 2:

from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ranks = defaultdict(int)

        for road in roads:
            ranks[road[0]] += 1
            ranks[road[1]] += 1

        maxrank = 0
        for i in range(n):
            for j in range(i + 1,  n):
                newrank = ranks[i] + ranks[j]
                if newrank > maxrank:
                    maxrank = newrank - (1 if [i, j] in roads or [j, i] in roads else 0)
        return maxrank


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        (4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4),
        (2, [[0, 1]], 1),
        (3, [], 0),
    ]
    passed = 0
    for n, roads, exp in TESTS:
        got = sol.maximalNetworkRank(n, roads)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
