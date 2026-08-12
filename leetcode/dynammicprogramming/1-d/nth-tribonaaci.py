# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
#
# T0=0, T1=1, T2=1, Tn = T(n-3)+T(n-2)+T(n-1)
#
# Example: n = 4 -> 4


def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    t0, t1, t2 = 0, 1, 1
    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(0, 0), (1, 1), (4, 4), (25, 1389537)]
    passed = 0
    for n, exp in TESTS:
        got = tribonacci(n)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
