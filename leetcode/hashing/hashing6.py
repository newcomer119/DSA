# Count Pairs with Absolute Difference K (i < j)
# GFG: https://www.geeksforgeeks.org/count-pairs-difference-equal-k/
#
# Count pairs (i, j) such that abs(arr[i] - arr[j]) == k and i < j.
#
# Example:
# arr = [1, 5, 3, 4, 2], k = 2 -> 3


def count_pairs_brute_force(arr: list[int], k: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                count += 1
    return count


def count_pairs(arr: list[int], k: int) -> int:
    count = 0
    freq_map = {}
    for num in arr:
        if num - k in freq_map:
            count += freq_map[num - k]
        if k != 0 and num + k in freq_map:
            count += freq_map[num + k]
        freq_map[num] = freq_map.get(num, 0) + 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 5, 3, 4, 2], 2, 3),
        ([1, 1, 1], 0, 3),
        ([1, 2, 3], 5, 0),
    ]
    passed = 0
    for arr, k, exp in TESTS:
        got = count_pairs(arr, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] arr={arr}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
