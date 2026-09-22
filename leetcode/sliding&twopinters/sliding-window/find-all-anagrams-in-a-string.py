# Given a string original and a string check, find the starting index of all substrings in original that are anagrams of check. Return the indices in ascending order.

# Parameters
# original: A string
# check: A string
# Result
# A list of integers representing the starting indices of all anagrams of check.
# Examples
# Example 1
# Input: original = "cbaebabacd", check = "abc"

# Output: [0, 6]

# Explanation: original[0:3] = "cba" and original[6:9] = "bac" each contain exactly the same letters as "abc" with different ordering.

# Example 2
# Input: original = "abab", check = "ab"

# Output: [0, 1, 2]

# Explanation: Every length-2 window in "abab" ("ab", "ba", "ab") is an anagram of "ab".

# Constraints
# 1 <= len(original), len(check) <= 10^5
# Each string consists of only lowercase characters in the standard English alphabet.

def find_all_anagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []

    pCount, sCount = {}, {}

    # Build frequency maps for p and first window of s
    for i in range(len(p)):
        pCount[p[i]] = pCount.get(p[i], 0) + 1
        sCount[s[i]] = sCount.get(s[i], 0) + 1

    res = [0] if sCount == pCount else []

    l = 0

    # Slide window through s
    for r in range(len(p), len(s)):
        # Add new character on right
        sCount[s[r]] = sCount.get(s[r], 0) + 1

        # Remove old character on left
        sCount[s[l]] -= 1

        if sCount[s[l]] == 0:
            sCount.pop(s[l])

        l += 1

        if sCount == pCount:
            res.append(l)

    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("cbaebabacd", "abc", [0, 6]),
             ("abab", "ab", [0, 1, 2]), ("a", "aa", [])]
    passed = 0
    for orig, check, exp in TESTS:
        got = find_all_anagrams(orig, check)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {orig}/{check} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
