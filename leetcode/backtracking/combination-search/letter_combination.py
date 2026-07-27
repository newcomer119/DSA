def letter_combination(n: int) -> list[str]:
    res = []
    def dfs(start_index,path):
        if start_index == n:
            res.append("".join(path))
            return 
        for letter in "ab":
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()
    dfs(0,[])
    return res
            


    
    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(letter_combination(2))
    ok = got == ["aa", "ab", "ba", "bb"]
    print(f"[{'PASS' if ok else 'FAIL'}] n=2 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
