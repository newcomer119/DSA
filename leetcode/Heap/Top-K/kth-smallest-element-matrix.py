# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
 

# Follow up:

# Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.


import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for r in range(min(n, k)):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        res = -1
        for _ in range(k):
            val, r, c = heapq.heappop(heap)
            res = val

            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return res


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
        ([[1, 2], [3, 4]], 2, 2),
        ([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 4, 6),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 5),
    ]
    passed = 0
    for matrix, k, expected in TESTS:
        got = sol.kthSmallest(matrix, k)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] k={k} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")
