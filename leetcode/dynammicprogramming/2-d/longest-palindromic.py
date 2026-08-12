# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Return the longest palindromic substring in s.
#
# Example: s = "babad" -> "bab" (or "aba")


def longest_palindrome(s: str) -> str:
    res = ""
    res_len = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l : r + 1]
                res_len = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l : r + 1]
                res_len = r - l + 1
            l -= 1
            r += 1
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
    ]
    passed = 0
    for s, exp_set in TESTS:
        got = longest_palindrome(s)
        ok = got in exp_set
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' -> '{got}'")
    print(f"\n{passed}/{len(TESTS)} passed")
