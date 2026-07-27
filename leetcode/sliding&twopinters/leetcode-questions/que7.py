# Given a string s, return the length of the longest substring that contains at most two distinct characters.

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.

# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters.


def lengthOfLongestSubstringTwoDistinct(s):
    last_occurrence = dict()
    max_len, l = 0, 0
    for r in range(len(s)):
        last_occurrence[s[r]] = r
        r += 1
        if len(last_occurrence) == 3:
            l = min(last_occurrence.values())+1
            del last_occurrence[s[l-1]]
        max_len = max(max_len, r - l)
    return max_len


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("eceba", 3), ("ccaabbb", 5), ("a", 1)]
    passed = 0
    for s, exp in TESTS:
        got = lengthOfLongestSubstringTwoDistinct(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")