# Element with Minimum and Maximum Frequency
# GFG: https://www.geeksforgeeks.org/element-with-minimum-and-maximum-frequency-in-an-array/
#
# Given an array, print one element with minimum frequency and one with maximum frequency.
# If multiple answers exist, return any valid pair.
#
# Example:
# arr = [1, 2, 2, 3, 3, 3]
# Output: (1, 3)

from collections import Counter


def min_max_frequency_elements(arr: list[int]) -> tuple[int, int]:
    freq = Counter(arr)
    min_elem = min(freq, key=lambda x: freq[x])
    max_elem = max(freq, key=lambda x: freq[x])
    return min_elem, max_elem


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 2, 3, 3, 3], (1, 3)),
        ([4, 4, 4, 4], (4, 4)),
        ([7, 8, 8, 9], (7, 8)),
    ]
    passed = 0
    for arr, exp in TESTS:
        got = min_max_frequency_elements(arr)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {arr} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
