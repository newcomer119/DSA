def generate_parentheses(n: int) -> list[str]:
    res= []
    path = []

    def dfs(start_index,open_count,close_count):
        if start_index == 2 * n:
            res.append("".join(path))
            return 

        if open_count < n:
            path.append("(")
            dfs(start_index + 1,open_count + 1, close_count)
            path.pop()


        if close_count < open_count:
            path.append(")")
            dfs(start_index + 1,open_count,close_count + 1)
            path.pop()


    dfs(0,0,0)
    return res

    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(generate_parentheses(2))
    ok = got == ["(())", "()()"]
    print(f"[{'PASS' if ok else 'FAIL'}] n=2 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
