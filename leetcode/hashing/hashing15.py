# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
#
# Return the index of the first non-repeating character in s, or -1 if none exists.
#
# Example:
# s = "leetcode" -> 0
# s = "loveleetcode" -> 2
# s = "aabb" -> -1


def first_unique_character(s: str) -> int:
    char_c = {}
    for char in s:
        char_c[char] = char_c.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_c[char] == 1:
            return i

    return -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ]
    passed = 0
    for s, exp in TESTS:
        got = first_unique_character(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
