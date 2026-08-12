# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#
# Balloons are horizontal segments [xstart, xend]. Min arrows to burst all.
#
# Example: [[10,16],[2,8],[1,6],[7,12]] -> 2


def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows = 0
    last_arrow = float("-inf")
    for start, end in points:
        if start > last_arrow:
            arrows += 1
            last_arrow = end
    return arrows


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ]
    passed = 0
    for points, exp in TESTS:
        got = find_min_arrow_shots(points)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] arrows -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
