# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
#
# Return length of longest strictly increasing subsequence.
#
# Example: nums = [10,9,2,5,3,7,101,18] -> 4


def length_of_lis(nums: list[int]) -> int:
    tails = []
    for num in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < num:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(num)
        else:
            tails[lo] = num
    return len(tails)


def length_of_lis_dp(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = length_of_lis(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums[:4]}... -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
