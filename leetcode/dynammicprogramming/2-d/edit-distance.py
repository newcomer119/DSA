# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/
#
# Minimum insert/delete/replace operations to convert word1 to word2.
#
# Example: word1 = "horse", word2 = "ros" -> 3


def min_distance(word1: str, word2: str) -> int:
    cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for j in range(len(word2) + 1):
        cache[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        cache[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
    return cache[0][0]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "a", 1),
    ]
    passed = 0
    for w1, w2, exp in TESTS:
        got = min_distance(w1, w2)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{w1}' -> '{w2}' = {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
