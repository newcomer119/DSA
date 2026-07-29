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


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    char_count = {}
    max_len = 0
    left =0 
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len


    # # Use a dictionary to keep track of character counts in the current window
    # char_count = {}
    # max_len = 0
    # left = 0
    
    # for right in range(len(s)):
    #     # Add the character at 'right' to the window
    #     char_count[s[right]] = char_count.get(s[right], 0) + 1
    #     # If we have more than 2 distinct characters, shrink the window
    #     while len(char_count) > 2:
    #         char_count[s[left]] -= 1
    #         if char_count[s[left]] == 0:
    #             del char_count[s[left]]
    #         left += 1
    #     # Update the maximum length
    #     max_len = max(max_len, right - left + 1)       
    # return max_len
 


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
