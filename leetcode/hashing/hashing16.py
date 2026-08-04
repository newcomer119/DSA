# 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/
#
# Given an array of strings, return all characters that appear in every string
# (including duplicates — as many times as the minimum frequency across words).
#
# Example:
# words = ["bella", "label", "roller"] -> ["e", "l", "l"]


def common_characters(words: list[str]) -> list[str]:
    freq = {}
    for char in words[0]:
        freq[char] = freq.get(char, 0) + 1

    for char in list(freq):
        for word in words[1:]:
            freq[char] = min(freq[char], word.count(char))

    res = []
    for char, count in freq.items():
        res.extend([char] * count)
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["bella", "label", "roller"], sorted(["e", "l", "l"])),
        (["cool", "lock", "cook"], sorted(["c", "o"])),
    ]
    passed = 0
    for words, exp in TESTS:
        got = sorted(common_characters(words))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {words} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
