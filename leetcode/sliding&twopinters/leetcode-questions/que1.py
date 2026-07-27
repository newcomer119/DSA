# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    l, r = 0, len(s)-1
    res = list(s)
    while l < r:
        if s[l] not in vowels:        # s[l] is not vowel
            l += 1
        elif s[r] not in vowels:      # s[r] is not vowel
            r -= 1
        else:
            res[l], res[r] = res[r], res[l]   # both vowels, swap
            l += 1
            r -= 1
    return "".join(res)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("IceCreAm", "AceCreIm"), ("leetcode", "leotcede"), ("bcdfg", "bcdfg")]
    passed = 0
    for s, exp in TESTS:
        got = reverseVowels(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s} -> {got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")