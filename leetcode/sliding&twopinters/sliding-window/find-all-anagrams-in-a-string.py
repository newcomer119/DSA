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


def find_all_anagrams(original: str, check: str) -> list[int]:
    original_len = len(original)
    check_len = len(check)

    if original_len < check_len:
        return []

    res = []
    check_counter = [0] *  26
    window = [0] * 26
    a = ord("a")

    for i in range(check_len):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1

    if window == check_counter:
        res.append(0)

    for i in range(check_len, original_len):
        window[ord(original[i - check_len]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            res.append(i - check_len + 1)

    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("cbaebabacd", "abc", [0, 6]), ("abab", "ab", [0, 1, 2]), ("a", "aa", [])]
    passed = 0
    for orig, check, exp in TESTS:
        got = find_all_anagrams(orig, check)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {orig}/{check} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")