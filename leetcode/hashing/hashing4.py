# Count Pairs with Sum Equal to K (i < j)
# GFG: https://www.geeksforgeeks.org/count-pairs-with-given-sum/
# LeetCode (two-sum style): https://leetcode.com/problems/two-sum/
#
# Count pairs (i, j) such that arr[i] + arr[j] == k and i < j.
#
# Example:
# arr = [1, 5, 7, -1, 5], k = 6 -> 3  (pairs: (0,1), (0,4), (1,4))


def count_pairs_brute_force(arr: list[int], k: int) -> int:
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    return count


def count_with_pairs(arr: list[int], k: int) -> int:
    count = 0
    freq = {}
    for num in arr:
        complement = k - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 5, 7, -1, 5], 6, 3),
        ([1, 1, 1], 2, 3),
        ([1, 2, 3], 7, 0),
    ]
    passed = 0
    for arr, k, exp in TESTS:
        got = count_with_pairs(arr, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] arr={arr}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
