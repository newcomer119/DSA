# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Given an unsorted array, return the length of the longest consecutive elements sequence.
# Must run in O(n) for the hash-set approach.
#
# Example:
# nums = [100, 4, 200, 1, 3, 2] -> 4  (sequence 1, 2, 3, 4)


def longest_consecutive_sequence(nums: list[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    n = len(nums)
    cs = 1
    ls = 1
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            continue
        if nums[i + 1] - nums[i] == 1:
            cs += 1
        else:
            cs = 1
        ls = max(ls, cs)
    return ls


def longest_consecutive_sequence_optimized(nums: list[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    max_streak = 0
    for x in num_set:
        if x - 1 not in num_set:
            current_num = x
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            max_streak = max(max_streak, current_streak)
    return max_streak


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = longest_consecutive_sequence_optimized(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
