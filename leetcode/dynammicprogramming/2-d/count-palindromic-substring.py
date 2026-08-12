# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
#
# Count all palindromic substrings in s.
#
# Example: s = "abc" -> 3


def count_substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("abc", 3), ("aaa", 6), ("a", 1)]
    passed = 0
    for s, exp in TESTS:
        got = count_substrings(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
