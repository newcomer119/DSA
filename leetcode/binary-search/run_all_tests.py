"""
Daily binary-search practice checker.

Run from this folder:
    python run_all_tests.py

Run one problem:
    python run_all_tests.py koko
    python run_all_tests.py first-true
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

FOLDER = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str | None = None):
    path = FOLDER / filename
    name = module_name or path.stem.replace(" ", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def test_first_true() -> tuple[int, int]:
    mod = load_module("FirstTrue.py")
    tests = [
        ("example", [False, False, True, True, True], 2),
        ("first is true", [True, True, True], 0),
        ("last is true", [False, False, True], 2),
        ("single false", [False], -1),
        ("single true", [True], 0),
    ]
    passed = 0
    for name, arr, expected in tests:
        if run_case(name, mod.find_boundary(arr), expected):
            passed += 1
    return passed, len(tests)


def test_first_not_smaller() -> tuple[int, int]:
    mod = load_module("First ElementNotSmallerThanTarget.py")
    tests = [
        ("example 1", [1, 3, 3, 5, 8, 8, 10], 2, 1),
        ("example 2", [2, 3, 5, 7, 11, 13, 17, 19], 6, 3),
        ("target larger than all", [1, 2, 3], 10, -1),
        ("target equals first", [5, 7, 9], 5, 0),
        ("target equals last", [1, 3, 5, 7], 7, 3),
    ]
    passed = 0
    for name, arr, target, expected in tests:
        if run_case(name, mod.first_not_smaller(arr, target), expected):
            passed += 1
    return passed, len(tests)


def test_find_first_occurrence() -> tuple[int, int]:
    mod = load_module("FindElementinSortedArraywithDuplicates.py")
    tests = [
        ("example found", [1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3, 1),
        ("example missing", [2, 3, 5, 7, 11, 13, 17, 19], 6, -1),
        ("single element hit", [7], 7, 0),
        ("single element miss", [7], 3, -1),
        ("target at end", [1, 2, 2, 2, 9], 9, 4),
    ]
    passed = 0
    for name, arr, target, expected in tests:
        if run_case(name, mod.find_first_occurrence(arr, target), expected):
            passed += 1
    return passed, len(tests)


def test_square_root() -> tuple[int, int]:
    mod = load_module("SquareRootEstimation.py")
    tests = [
        ("perfect square", 16, 4),
        ("truncate", 8, 2),
        ("zero", 0, 0),
        ("one", 1, 1),
        ("large", 26, 5),
    ]
    passed = 0
    for name, n, expected in tests:
        if run_case(name, mod.square_root(n), expected):
            passed += 1
    return passed, len(tests)


def test_find_min_rotated() -> tuple[int, int]:
    mod = load_module("FindMinimuminRotatedSortedArray.py")
    tests = [
        ("example 1", [30, 40, 50, 10, 20], 3),
        ("example 2", [3, 5, 7, 11, 13, 17, 19, 2], 7),
        ("no rotation", [1, 2, 3, 4, 5], 0),
        ("two elements rotated", [2, 1], 1),
        ("two elements sorted", [1, 2], 0),
    ]
    passed = 0
    for name, arr, expected in tests:
        if run_case(name, mod.find_min_rotated(arr), expected):
            passed += 1
    return passed, len(tests)


def test_peak_of_mountain() -> tuple[int, int]:
    mod = load_module("ThePeakofMountainArray.py")
    tests = [
        ("example", [0, 1, 2, 3, 2, 1, 0], 3),
        ("small mountain", [1, 3, 2], 1),
        ("peak near start", [1, 5, 4, 3], 1),
        ("peak near end", [1, 2, 3, 4, 2], 3),
    ]
    passed = 0
    for name, arr, expected in tests:
        if run_case(name, mod.peak_of_mountain_array(arr), expected):
            passed += 1
    return passed, len(tests)


def test_newspapers() -> tuple[int, int]:
    mod = load_module("Newspaper.py")
    tests = [
        ("example 1", [7, 2, 5, 10, 8], 2, 18),
        ("example 2", [2, 3, 5, 7], 3, 7),
        ("one worker", [4, 5, 6], 1, 15),
        ("each paper one worker", [4, 5, 6], 3, 6),
        ("single paper", [10], 5, 10),
    ]
    passed = 0
    for name, times, workers, expected in tests:
        if run_case(name, mod.newspapers_split(times, workers), expected):
            passed += 1
    return passed, len(tests)


def test_first_bad_version() -> tuple[int, int]:
    mod = load_module("first-bad-version.py")

    class Solution:
        def firstBadVersion(self, n, bad):
            def isBadVersion(version):
                return version >= bad

            l, r, ans = 0, n, -1
            while l <= r:
                mid = (l + r) // 2
                if isBadVersion(mid):
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

    sol = Solution()
    tests = [
        ("example 1", 5, 4, 4),
        ("example 2", 1, 1, 1),
        ("first version bad", 10, 1, 1),
        ("last version bad", 10, 10, 10),
    ]
    passed = 0
    for name, n, bad, expected in tests:
        if run_case(name, sol.firstBadVersion(n, bad), expected):
            passed += 1
    return passed, len(tests)


def test_search_range() -> tuple[int, int]:
    mod = load_module("find-first-and-last-position-of-element-in-sorted-array.py")

    class Solution:
        searchRange = mod.searchRange

    sol = Solution()
    tests = [
        ("found range", [5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ("missing", [5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ("all same", [2, 2, 2, 2], 2, [0, 3]),
        ("single hit", [1], 1, [0, 0]),
        ("single miss", [1], 2, [-1, -1]),
    ]
    passed = 0
    for name, nums, target, expected in tests:
        if run_case(name, list(sol.searchRange(nums, target)), expected):
            passed += 1
    return passed, len(tests)


def test_single_non_duplicate() -> tuple[int, int]:
    mod = load_module("single-element-in-a-sorted-array.py")

    class Solution:
        singleNonDuplicate = mod.singleNonDuplicate

    sol = Solution()
    tests = [
        ("example 1", [1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ("example 2", [3, 3, 7, 7, 10, 11, 11], 10),
        ("single element", [9], 9),
        ("unique at end", [1, 1, 2, 2, 3], 3),
        ("unique at start", [1, 2, 2, 3, 3], 1),
    ]
    passed = 0
    for name, nums, expected in tests:
        if run_case(name, sol.singleNonDuplicate(nums), expected):
            passed += 1
    return passed, len(tests)


def test_koko() -> tuple[int, int]:
    mod = load_module("koko-eating-bananas.py")

    class Solution:
        can_finish_eating = mod.can_finish_eating
        minEatingSpeed = mod.minEatingSpeed

    sol = Solution()
    tests = [
        ("example 1", [3, 6, 7, 11], 8, 4),
        ("example 2", [30, 11, 23, 4, 20], 5, 30),
        ("example 3", [30, 11, 23, 4, 20], 6, 23),
        ("one pile", [10], 5, 2),
        ("many hours available", [3, 6, 7, 11], 11, 3),
    ]
    passed = 0
    for name, piles, h, expected in tests:
        if run_case(name, sol.minEatingSpeed(piles, h), expected):
            passed += 1
    return passed, len(tests)


def test_my_calendar() -> tuple[int, int]:
    mod = load_module("my-calendar-i.py")
    tests = [
        (
            "example sequence",
            [(10, 20), (15, 25), (20, 30)],
            [True, False, True],
        ),
        (
            "touching ends allowed",
            [(1, 5), (5, 10), (10, 15)],
            [True, True, True],
        ),
        (
            "overlap rejected",
            [(2, 8), (3, 9)],
            [True, False],
        ),
    ]
    passed = 0
    for name, bookings, expected in tests:
        cal = mod.MyCalendar()
        actual = [cal.book(s, e) for s, e in bookings]
        if run_case(name, actual, expected):
            passed += 1
    return passed, len(tests)


def test_snapshot_array() -> tuple[int, int]:
    mod = load_module("snapshot-array.py")
    passed = 0
    total = 2

    arr = mod.SnapshotArray(3)
    arr.set(0, 5)
    snap0 = arr.snap()
    arr.set(0, 6)
    if run_case("leetcode example", arr.get(0, snap0), 5):
        passed += 1

    arr2 = mod.SnapshotArray(2)
    arr2.set(1, 8)
    snap0 = arr2.snap()
    arr2.set(1, 12)
    snap1 = arr2.snap()
    ok = run_case("multiple snaps index 1 snap0", arr2.get(1, snap0), 8)
    ok = run_case("multiple snaps index 1 snap1", arr2.get(1, snap1), 12) and ok
    ok = run_case("untouched index stays 0", arr2.get(0, snap1), 0) and ok
    if ok:
        passed += 1

    return passed, total


def test_plates_between_candles() -> tuple[int, int]:
    mod = load_module("plates_between_candles.py")

    class Solution:
        platesBetweenCandles = mod.Solution.platesBetweenCandles

    sol = Solution()
    tests = [
        ("example 1", "**|**|***|", [[2, 5], [5, 9]], [2, 3]),
        (
            "example 2",
            "***|**|*****|**||**|*",
            [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
            [9, 0, 0, 0, 0],
        ),
        ("no candles in range", "*|**|*", [[0, 0], [3, 3]], [0, 0]),
        ("plates but one candle", "*|***", [[0, 4]], [0]),
    ]
    passed = 0
    for name, s, queries, expected in tests:
        if run_case(name, sol.platesBetweenCandles(s, queries), expected):
            passed += 1
    return passed, len(tests)


def test_time_map() -> tuple[int, int]:
    mod = load_module("time-based-key-value-store.py")
    tm = mod.TimeMap()
    tm.set("foo", "bar", 1)
    tests = [
        ("get at exact time", tm.get("foo", 1), "bar"),
        ("get before next set", tm.get("foo", 3), "bar"),
    ]
    tm.set("foo", "bar2", 4)
    tests.extend([
        ("get at new time", tm.get("foo", 4), "bar2"),
        ("get after new time", tm.get("foo", 5), "bar2"),
        ("missing key", tm.get("missing", 1), ""),
        ("time before first set", tm.get("foo", 0), ""),
    ])
    passed = 0
    for name, actual, expected in tests:
        if run_case(name, actual, expected):
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "first-true": ("FirstTrue.py", test_first_true),
    "first-not-smaller": ("First ElementNotSmallerThanTarget.py", test_first_not_smaller),
    "find-first-occurrence": ("FindElementinSortedArraywithDuplicates.py", test_find_first_occurrence),
    "square-root": ("SquareRootEstimation.py", test_square_root),
    "find-min-rotated": ("FindMinimuminRotatedSortedArray.py", test_find_min_rotated),
    "peak-mountain": ("ThePeakofMountainArray.py", test_peak_of_mountain),
    "newspaper": ("Newspaper.py", test_newspapers),
    "first-bad-version": ("first-bad-version.py", test_first_bad_version),
    "search-range": ("find-first-and-last-position-of-element-in-sorted-array.py", test_search_range),
    "single-element": ("single-element-in-a-sorted-array.py", test_single_non_duplicate),
    "koko": ("koko-eating-bananas.py", test_koko),
    "my-calendar": ("my-calendar-i.py", test_my_calendar),
    "snapshot-array": ("snapshot-array.py", test_snapshot_array),
    "plates-between-candles": ("plates_between_candles.py", test_plates_between_candles),
    "time-map": ("time-based-key-value-store.py", test_time_map),
}


def main() -> int:
    filters = [arg.lower() for arg in sys.argv[1:]]

    if filters:
        selected = {k: v for k, v in ALL_TESTS.items() if any(f in k for f in filters)}
        if not selected:
            print("No matching problems. Available keys:")
            for key in ALL_TESTS:
                print(f"  - {key}")
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed_problems = []

    print("=" * 60)
    print("Binary Search Daily Tests")
    print("=" * 60)

    for key, (_, runner) in selected.items():
        print(f"\n{key}")
        print("-" * len(key))
        passed, count = runner()
        total_passed += passed
        total_cases += count
        if passed != count:
            failed_problems.append(key)

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_cases} test groups passed")
    if failed_problems:
        print("Needs review:", ", ".join(failed_problems))
        return 1

    print("All tests passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
