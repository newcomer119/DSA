# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
#
# Match s against pattern p with '.' and '*' support.
#
# Example: s = "aa", p = "a*" -> True


def is_match(s: str, p: str) -> bool:
    cache = {}

    def dfs(i: int, j: int) -> bool:
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        if j + 1 < len(p) and p[j + 1] == "*":
            cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            return cache[(i, j)]
        if match:
            cache[(i, j)] = dfs(i + 1, j + 1)
            return cache[(i, j)]
        cache[(i, j)] = False
        return False

    return dfs(0, 0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
    ]
    passed = 0
    for s, p, exp in TESTS:
        got = is_match(s, p)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' ~ '{p}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
