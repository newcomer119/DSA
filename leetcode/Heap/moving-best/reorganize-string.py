
# 767. Reorganize String
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


from collections import Counter
from heapq import heappop, heappush, heapify


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, ch) for ch, freq in count.items()]
        heapify(max_heap)

        prev_freq = 0
        prev_char = ""
        result = []

        while max_heap:
            freq, ch = heappop(max_heap)
            freq = -freq
            result.append(ch)
            freq -= 1

            if prev_freq > 0:
                heappush(max_heap, (-prev_freq, prev_char))

            prev_freq = freq
            prev_char = ch

        return "".join(result) if len(result) == len(s) else ""


def valid_reorg(s, result):
    if Counter(s) != Counter(result):
        return False
    for i in range(len(result) - 1):
        if result[i] == result[i + 1]:
            return False
    return True


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        ("aab", "aba"),
        ("aaab", ""),
        ("aabb", None),
        ("vvvlo", None),
        ("abc", None),
    ]
    passed = 0
    for s, expected in TESTS:
        got = sol.reorganizeString(s)
        if expected is None:
            ok = got != "" and valid_reorg(s, got)
        else:
            ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s!r} -> {got!r}" + (f" (expected {expected!r})" if expected is not None else ""))
    print(f"\n{passed}/{len(TESTS)} passed")
