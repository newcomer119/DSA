def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res: list[list[int]] = []

    def dfs(nums: list[int], start_index: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start_index, len(nums)):
            num = nums[i]
            if remaining - num < 0:
                break
            path.append(num)
            dfs(nums, i, remaining - num, path)
            path.pop()

    candidates.sort()
    dfs(candidates, 0, target, [])
    return res

    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(map(tuple, combination_sum([2, 3, 5], 8)))
    exp = sorted(map(tuple, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] combination_sum target=8 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
