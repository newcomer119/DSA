# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
#
# Merge all overlapping intervals.
#
# Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for current in intervals:
        if not merged or current[0] > merged[-1][1]:
            merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    return merged


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[4, 7], [1, 4]], [[1, 7]]),
    ]
    passed = 0
    for intervals, exp in TESTS:
        got = merge(intervals)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] merge -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
