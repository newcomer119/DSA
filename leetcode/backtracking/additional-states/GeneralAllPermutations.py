def permutations(letters: str) -> list[str]:
    res = []
    path = []
    used = [False] * len(letters)

    def dfs(start_index):
        if start_index == len(letters):
            res.append("".join(path))
            return 


        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(start_index + 1)
            path.pop()
            used[i] = False
    dfs(0)
    return res
        

    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(permutations("ab"))
    ok = got == ["ab", "ba"]
    print(f"[{'PASS' if ok else 'FAIL'}] permutations('ab') -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
