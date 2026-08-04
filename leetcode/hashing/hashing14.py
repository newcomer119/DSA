# Maximum Distance Between Two Equal Elements
# GFG: https://www.geeksforgeeks.org/maximum-distance-between-two-occurrences-of-same-element-in-array/
# LeetCode: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/  (different variant)
#
# Given an array, return the maximum distance between two indices i and j
# such that arr[i] == arr[j] and i < j.
#
# Example:
# arr = [1, 2, 3, 2, 1] -> 3  (distance between indices 1 and 3 for value 2)


def max_distance(arr: list[int]) -> int:
    freq = {}
    dist = 0
    for i, num in enumerate(arr):
        if num not in freq:
            freq[num] = i
        else:
            dist = max(dist, i - freq[num])
    return dist


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3, 2, 1], 4),
        ([1, 1, 1, 1], 3),
        ([1, 2, 3, 4], 0),
    ]
    passed = 0
    for arr, exp in TESTS:
        got = max_distance(arr)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {arr} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
