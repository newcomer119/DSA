
# 263. Ugly Number
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for prime in (2, 3, 5):
            while n % prime == 0:
                n //= prime
        return n == 1


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        (6, True),
        (1, True),
        (14, False),
        (8, True),
        (0, False),
        (-6, False),
        (30, True),
    ]
    passed = 0
    for n, expected in TESTS:
        got = sol.isUgly(n)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")
