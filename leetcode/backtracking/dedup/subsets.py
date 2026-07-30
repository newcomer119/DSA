def subsets(nums: list[int]) -> list[list[int]]:
    # res = []
    # def dfs(start_index,cur):
    #     if start_index == len(nums):
    #         res.append(cur[:])
    #         return 

    #     cur.append(nums[start_index])
    #     dfs(start_index + 1, cur)
    #     cur.pop()
    #     dfs(start_index + 1, cur)
        
    # dfs(0,[])
    # return res

    res = []
    def dfs(start_index,cur):
        if start_index == len(nums):
            res.append(cur[:])
            return 
        cur.append(nums[start_index])
        dfs(start_index + 1,cur)
        cur.pop()
        dfs(start_index + 1, cur)
    dfs(0,[])
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 2], 4), ([1], 2), ([], 1)]
    passed = 0
    for nums, exp_len in TESTS:
        got = subsets(nums)
        ok = len(got) == exp_len
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {len(got)} subsets")
    print(f"\n{passed}/{len(TESTS)} passed")
