# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
#
# Return true if t is an anagram of s (same characters, same counts).
#
# Example:
# s = "anagram", t = "nagaram" -> True
# s = "rat", t = "car" -> False


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    for char in t:
        if char not in freq_map:
            return False
        freq_map[char] -= 1
        if freq_map[char] < 0:
            return False

    return True


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
    ]
    passed = 0
    for s, t, exp in TESTS:
        got = valid_anagram(s, t)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' vs '{t}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
