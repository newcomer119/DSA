# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
#
# Count distinct subsequences of s that equal t.
#
# Example: s = "rabbbit", t = "rabbit" -> 3


def num_distinct(s: str, t: str) -> int:
    cache = {}

    def dfs(i: int, j: int) -> int:
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        if s[i] == t[j]:
            cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            cache[(i, j)] = dfs(i + 1, j)
        return cache[(i, j)]

    return dfs(0, 0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
        ("a", "a", 1),
    ]
    passed = 0
    for s, t, exp in TESTS:
        got = num_distinct(s, t)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' -> '{t}' = {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
