# Frequency Queries on an Array
# GFG: https://www.geeksforgeeks.org/queries-for-counts-of-array-elements/
#
# Given an array and Q queries, each query asks for the frequency of a number X in the array.
#
# Example:
# arr = [1, 2, 1, 3, 2, 1], queries = [1, 2, 4]
# Output: [3, 2, 0]

from collections import defaultdict


def query_frequencies(arr: list[int], queries: list[int]) -> list[int]:
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    return [freq[q] for q in queries]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 1, 3, 2, 1], [1, 2, 4], [3, 2, 0]),
        ([5, 5, 5], [5, 1], [3, 0]),
        ([], [1], [0]),
    ]
    passed = 0
    for arr, queries, exp in TESTS:
        got = query_frequencies(arr, queries)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] queries={queries} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
