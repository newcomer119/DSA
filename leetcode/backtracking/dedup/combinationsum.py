# Combination Sum
# Prereq: Backtracking

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7

# Output: [[2,2,3],[7]]

# Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.

# 7 is a candidate, and 7 = 7.

# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8

# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1

# Output: []

# Example 4:
# Input: candidates = [1], target = 1

# Output: [[1]]

# Example 5:
# Input: candidates = [1], target = 2

# Output: [[1, 1]]

# Constrains:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500



def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res: list[list[int]] = []
    def dfs(nums,start_index,remaining,path):
        if remaining == 0:
            res.append(path[:])
            return 

        for i in range(start_index, len(nums)):
            num = nums[i]
            if remaining - num < 0:
                break

            path.append(num)
            dfs(nums,i,remaining-num,path)
            path.pop()

    candidates.sort()
    dfs(candidates,0,target,[])
    return res
    # def dfs(nums: list[int], start_index: int, remaining: int, path: list[int]) -> None:
    #     if remaining == 0:
    #         res.append(path[:])
    #         return
    #     for i in range(start_index, len(nums)):
    #         num = nums[i]
    #         if remaining - num < 0:
    #             break
    #         path.append(num)
    #         dfs(nums, i, remaining - num, path)
    #         path.pop()

    # candidates.sort()
    # dfs(candidates, 0, target, [])
    # return res



# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(map(tuple, combination_sum([2, 3, 5], 8)))
    exp = sorted(map(tuple, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] combination_sum target=8 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
