# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

# Constraints:

# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104
# Question

from typing import List

def numRescueBoats(self, people: List[int], limit: int) -> int:
      people.sort()
      l, r = 0 , len(people)-1
      boat = 0
      while l <= r:
          if people[l] + people[r] <= limit:
              l += 1
          boat += 1
          r -= 1
      return boat


# --- Daily tests ---
if __name__ == "__main__":
    class Solution:
        numRescueBoats = numRescueBoats

    sol = Solution()
    TESTS = [([1, 2], 3, 1), ([3, 2, 2, 1], 3, 3), ([3, 5, 3, 4], 5, 4)]
    passed = 0
    for people, limit, exp in TESTS:
        got = sol.numRescueBoats(people[:], limit)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {people}, limit={limit} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")