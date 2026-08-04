# Count Subarrays with XOR Equal to K
# GFG: https://www.geeksforgeeks.org/count-subarrays-having-a-given-xor-value/
# LeetCode (related): https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
#
# Count contiguous subarrays whose XOR equals k.
#
# Example:
# arr = [4, 2, 2, 6, 4], k = 6 -> 4


def subarrays_xor(arr: list[int], k: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n):
        curr_xor = 0
        for j in range(i, n):
            curr_xor ^= arr[j]
            if curr_xor == k:
                count += 1
    return count


def subarrays_xor_optimized(nums: list[int], k: int) -> int:
    prefix = {0: 1}
    curr_xor = 0
    total_subarr = 0
    for num in nums:
        curr_xor ^= num
        target_xor = curr_xor ^ k
        if target_xor in prefix:
            total_subarr += prefix[target_xor]
        prefix[curr_xor] = prefix.get(curr_xor, 0) + 1
    return total_subarr


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([4, 2, 2, 6, 4], 6, 4),
        ([5, 6, 7, 8, 9], 5, 2),
        ([1, 2, 3], 0, 1),
    ]
    passed = 0
    for arr, k, exp in TESTS:
        got = subarrays_xor_optimized(arr, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] arr={arr}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
