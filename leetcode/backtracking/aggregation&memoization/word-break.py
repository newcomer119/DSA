def word_break(s: str, words: list[str]) -> bool:
    memo  = {}
    def dfs(start_index):
        if start_index == len(s):
            return True
        if start_index in memo:
            return memo[start_index]
        ans = False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ans = True
                    break
        memo[start_index] = ans
        return ans
    return dfs(0)
    
    # memo : dict[int,bool] = {}
    # def dfs(start_index):
    #     if start_index == len(s):
    #         return True
    #     if start_index in memo:
    #         return memo[start_index]
    #     ans = False
    #     for word in words:
    #         if s[start_index:].startswith(word):
    #             if dfs(start_index + len(word)):
    #                 ans = True
    #                 break
    #     memo[start_index] = ans
    #     return ans
    # return dfs(0)



# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("leetcode", ["leet", "code"], True), ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)]
    passed = 0
    for s, words, exp in TESTS:
        got = word_break(s, words)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
