# 532. K-diff Pairs in an Array (difference version)
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
#
# Count pairs (i, j) such that arr[i] - arr[j] == k and i < j.
# Equivalent to counting pairs with difference k where the larger index holds the larger value.
#
# Example:
# arr = [3, 1, 4, 1, 5], k = 2 -> 2  (pairs: (2,0), (4,2))


def count_pairs_brute_force(arr: list[int], k: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] - arr[j] == k:
                count += 1
    return count


def count_with_pairs(arr: list[int], k: int) -> int:
    count = 0
    freq_map = {}
    for num in arr:
        target = num + k
        count += freq_map.get(target, 0)
        freq_map[num] = freq_map.get(num, 0) + 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3], 1, 0),
        ([1, 1, 1], 0, 3),
    ]
    passed = 0
    for arr, k, exp in TESTS:
        got = count_with_pairs(arr, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] arr={arr}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
