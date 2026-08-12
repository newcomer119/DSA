# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
#
# Return length of longest common subsequence of two strings.
#
# Example: text1 = "abcde", text2 = "ace" -> 3


def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ]
    passed = 0
    for t1, t2, exp in TESTS:
        got = longest_common_subsequence(t1, t2)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{t1}' vs '{t2}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
