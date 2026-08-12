# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
#
# Return minimum intervals to remove so the rest don't overlap.
# Touching endpoints ([1,2] and [2,3]) count as non-overlapping.
#
# Example: [[1,2],[2,3],[3,4],[1,3]] -> 1


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    kept = 0
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:
            kept += 1
            last_end = end
    return len(intervals) - kept


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]
    passed = 0
    for intervals, exp in TESTS:
        got = erase_overlap_intervals(intervals)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] remove -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
