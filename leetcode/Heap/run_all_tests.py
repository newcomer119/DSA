"""
Daily heap practice checker.

Run all tests:
    python run_all_tests.py

Run one problem:
    python run_all_tests.py kth-largest
    python run_all_tests.py median
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def norm_points(points):
    return sorted(tuple(p) for p in points)


def test_kth_largest() -> tuple[int, int]:
    mod = load_module("Top-K/kth-largest-element.py")
    sol = mod.Solution()
    tests = [
        ("example 1", [3, 2, 1, 5, 6, 4], 2, 5),
        ("example 2", [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ("single element", [1], 1, 1),
        ("two elements", [2, 1], 1, 2),
        ("k equals length", [7, 6, 5], 3, 5),
    ]
    passed = 0
    for name, nums, k, expected in tests:
        if run_case(name, sol.findKthLargest(nums, k), expected):
            passed += 1
    return passed, len(tests)


def test_k_closest() -> tuple[int, int]:
    mod = load_module("Top-K/k-closest-to-origin.py")
    sol = mod.Solution()
    tests = [
        ("example 1", [[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ("example 2", [[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ("k equals n", [[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
        ("closest single", [[1, 1], [2, 2], [3, 3]], 1, [[1, 1]]),
        ("origin included", [[-1, -1], [2, 2], [0, 0]], 2, [[0, 0], [-1, -1]]),
    ]
    passed = 0
    for name, points, k, expected in tests:
        got = sol.kClosest(points, k)
        if run_case(name, norm_points(got), norm_points(expected)):
            passed += 1
    return passed, len(tests)


def test_kth_smallest_matrix() -> tuple[int, int]:
    mod = load_module("Top-K/kth-smallest-element-matrix.py")
    sol = mod.Solution()
    tests = [
        ("example 1", [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ("example 2", [[-5]], 1, -5),
        ("2x2 matrix", [[1, 2], [3, 4]], 2, 2),
        ("k = 4", [[1, 3, 5], [6, 7, 12], [11, 14, 14]], 4, 6),
        ("sorted matrix", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 5),
    ]
    passed = 0
    for name, matrix, k, expected in tests:
        if run_case(name, sol.kthSmallest(matrix, k), expected):
            passed += 1
    return passed, len(tests)


def test_merge_k_lists() -> tuple[int, int]:
    mod = load_module("Top-K/merge-k-sorted-list.py")
    sol = mod.Solution()
    tests = [
        ("example 1", [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ("empty input", [], []),
        ("single empty list", [[]], []),
        ("three singletons", [[1], [2], [3]], [1, 2, 3]),
        ("with empty middle list", [[0, 2], [], [1]], [0, 1, 2]),
    ]
    passed = 0
    for name, arrays, expected in tests:
        lists = [mod.build_list(arr) for arr in arrays]
        got = mod.list_to_array(sol.mergeKLists(lists))
        if run_case(name, got, expected):
            passed += 1
    return passed, len(tests)


def test_reorganize_string() -> tuple[int, int]:
    mod = load_module("moving-best/reorganize-string.py")
    sol = mod.Solution()
    tests = [
        ("example valid", "aab", "aba"),
        ("example impossible", "aaab", ""),
        ("even counts", "aabb", None),
        ("three-way mix", "vvvlo", None),
        ("all unique", "abc", None),
    ]
    passed = 0
    for name, s, expected in tests:
        got = sol.reorganizeString(s)
        if expected is None:
            ok = got != "" and mod.valid_reorg(s, got)
            print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
            if not ok:
                print(f"         got: {got!r}")
        else:
            ok = run_case(name, got, expected)
        if ok:
            passed += 1
    return passed, len(tests)


def test_ugly_number() -> tuple[int, int]:
    mod = load_module("moving-best/ugly-number.py")
    sol = mod.Solution()
    tests = [
        ("example 1", 6, True),
        ("example 2", 1, True),
        ("example 3", 14, False),
        ("power of two", 8, True),
        ("zero", 0, False),
        ("negative", -6, False),
        ("only 2 3 5 factors", 30, True),
    ]
    passed = 0
    for name, n, expected in tests:
        if run_case(name, sol.isUgly(n), expected):
            passed += 1
    return passed, len(tests)


def test_median_finder() -> tuple[int, int]:
    mod = load_module("multiple-heaps/median.py")

    def run_sequence(nums):
        mf = mod.MedianFinder()
        medians = []
        for num in nums:
            mf.addNum(num)
            medians.append(mf.findMedian())
        return medians

    tests = [
        ("leetcode example", [1, 2, 3], [1.0, 1.5, 2.0]),
        ("even growing stream", [2, 3, 4, 5], [2.0, 2.5, 3.0, 3.5]),
        ("single value", [5], [5.0]),
        ("insert middle order", [1, 3, 2], [1.0, 2.0, 2.0]),
        ("negative numbers", [-1, -2, -3], [-1.0, -1.5, -2.0]),
    ]
    passed = 0
    for name, nums, expected in tests:
        got = run_sequence(nums)
        ok = all(abs(a - b) < 1e-5 for a, b in zip(got, expected))
        if ok:
            print(f"  [PASS] {name}")
        else:
            print(f"  [FAIL] {name}")
            print(f"         expected: {expected!r}")
            print(f"         got:      {got!r}")
        if ok:
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "kth-largest": ("Top-K/kth-largest-element.py", test_kth_largest),
    "k-closest": ("Top-K/k-closest-to-origin.py", test_k_closest),
    "kth-smallest-matrix": ("Top-K/kth-smallest-element-matrix.py", test_kth_smallest_matrix),
    "merge-k-lists": ("Top-K/merge-k-sorted-list.py", test_merge_k_lists),
    "reorganize-string": ("moving-best/reorganize-string.py", test_reorganize_string),
    "ugly-number": ("moving-best/ugly-number.py", test_ugly_number),
    "median": ("multiple-heaps/median.py", test_median_finder),
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
    print("Heap Daily Tests")
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
