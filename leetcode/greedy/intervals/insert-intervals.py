# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
#
# Insert newInterval into sorted non-overlapping intervals (merge if needed).
#
# Example: intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    res = []
    for current in intervals:
        if current[1] < new_interval[0]:
            res.append(current)
        elif current[0] > new_interval[1]:
            res.append(new_interval)
            new_interval = current
        else:
            new_interval[0] = min(new_interval[0], current[0])
            new_interval[1] = max(new_interval[1], current[1])
    res.append(new_interval)
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
    ]
    passed = 0
    for intervals, new_iv, exp in TESTS:
        got = insert(intervals, new_iv)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] insert -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
