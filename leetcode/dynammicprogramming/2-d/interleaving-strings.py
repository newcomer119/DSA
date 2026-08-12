# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/
#
# Return true if s3 is formed by interleaving s1 and s2.
#
# Example: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" -> True


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ]
    passed = 0
    for s1, s2, s3, exp in TESTS:
        got = is_interleave(s1, s2, s3)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] interleave -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
