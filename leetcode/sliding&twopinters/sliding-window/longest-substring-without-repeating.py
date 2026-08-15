# Longest Substring without Repeating Characters
# Find the length of the longest substring of a given string without repeating characters.
# Input: abccabcabcc
# Output: 3
# Explanation: The longest substrings are abc and cab, both of length 3.
# Use the "Sample 1: abccabcabcc" preset in the visualizer below to replay this case.
# Input: aaaabaaa
# Output: 2
# Explanation: ab is the longest substring, with a length of 2.


def longest_substring_without_repeating_characters(s: str) -> int:
    longest = 0
    left = 0
    window = set()
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1

        window.add(s[right])
        longest = max(longest , right - left + 1)

    return longest 
    # longest = 0
    # left = 0
    # window = set()

    # for r in range(len(s)):
    #     while s[r] in window:
    #         window.remove(s[left])
    #         left += 1

    #     window.add(s[r])
    #     longest = max(longest , r-left + 1)

    # return longest 
    

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("abccabcabcc", 3), ("aaaabaaa", 2), ("abcabcbb", 3), ("a", 1)]
    passed = 0
    for s, exp in TESTS:
        got = longest_substring_without_repeating_characters(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s!r} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")