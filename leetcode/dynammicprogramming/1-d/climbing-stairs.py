# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
#
# Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.
#
# Example: n = 3 -> 3


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev1, prev2 = 1, 2
    for _ in range(3, n + 1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(1, 1), (2, 2), (3, 3), (5, 8)]
    passed = 0
    for n, exp in TESTS:
        got = climb_stairs(n)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
