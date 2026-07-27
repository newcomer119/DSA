# 680. Valid Palindrome II
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.




class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(word):
            return word == word[::-1]
            
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l+1 : r+1]) or isPalindrome(s[l:r])

            l += 1
            r -= 1

        return True


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("aba", True), ("abca", True), ("abc", False), ("racecar", True)]
    sol = Solution()
    passed = 0
    for s, exp in TESTS:
        got = sol.validPalindrome(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")