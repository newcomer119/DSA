# Count Good Subarrays (sum % k == subarray length)
# Practice problem — brute force with prefix-style thinking.
#
# A subarray [i..j] is "good" if sum(nums[i..j]) % k == (j - i + 1).
#
# Note: This condition is NOT the same as (sum - length) % k == 0 when length >= k,
# so a simple prefix-hash O(n) trick does not apply directly. Use the nested loop approach.
#
# Example:
# nums = [1, 2, 3], k = 2 -> 2 good subarrays


def good_subarrays(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum % k == j - i + 1:
                count += 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([3, 1, 9, 6], 3, 1),
        ([1, 2, 3], 2, 2),
        ([0, 0], 1, 0),
    ]
    passed = 0
    for nums, k, exp in TESTS:
        got = good_subarrays(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] nums={nums}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
