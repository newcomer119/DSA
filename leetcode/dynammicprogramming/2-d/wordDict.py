# 139. Word Break
# https://leetcode.com/problems/word-break/
#
# Return true if s can be segmented into dictionary words.
#
# Example: s = "leetcode", wordDict = ["leet", "code"] -> True


def word_break(s: str, word_dict: list[str]) -> bool:
    memo = {}

    def dfs(start: int) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for word in word_dict:
            if s[start:].startswith(word) and dfs(start + len(word)):
                memo[start] = True
                return True
        memo[start] = False
        return False

    return dfs(0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]
    passed = 0
    for s, words, exp in TESTS:
        got = word_break(s, words)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
