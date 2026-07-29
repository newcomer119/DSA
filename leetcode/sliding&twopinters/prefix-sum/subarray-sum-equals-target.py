# This problem applies the prefix sum technique from the introduction: instead of testing every possible subarray, a running prefix sum turns the search into a hash table lookup.
# Given an integer array arr and a target value, return a subarray whose sum equals the target. Return the answer as [start, end), where start is inclusive and end is exclusive. If there are multiple valid answers, return the one with the smaller end value.
# Input: arr = [1, -20, -3, 30, 5, 4], target = 7
# Output: [1, 4]
# The subarray arr[1:4] = [-20, -3, 30] sums to 7.


def subarray_sum(nums: list[int], target: int) -> list[int]:
    # prefix_sum = {0:0}
    # curr_sum = 0
    # for i in range(len(nums)):
    #     curr_sum += nums[i]
    #     complement = curr_sum - target
    #     if complement in prefix_sum:
    #         return [prefix_sum[complement], i+1]
    #     prefix_sum[curr_sum] = i + 1
    # return []

    prefix = {0 : 0}
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        complement = curr_sum - target
        if complement in prefix:
            return[prefix[complement], i + 1]
        prefix[curr_sum] = i + 1

    return []


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, -20, -3, 30, 5, 4], 7, [1, 4]), ([1, 2, 3], 5, [1, 3]), ([1, 2, 3], 10, [])]
    passed = 0
    for nums, target, exp in TESTS:
        got = subarray_sum(nums, target)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")