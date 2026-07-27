def partition(s: str) -> list[list[str]]:
    ans = []
    n = len(s)
    def is_palindrome(word):
        return word == word[::-1]
    def dfs(start,path):
        if start == n:
            ans.append(path[:])
            return 
        for end in range(start + 1, n + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end,path + [prefix])

    dfs(0,[])
    return ans
        
    

    return ans


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(map(tuple, partition("aab")))
    exp = sorted(map(tuple, [["a", "a", "b"], ["aa", "b"]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] partition('aab') -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
