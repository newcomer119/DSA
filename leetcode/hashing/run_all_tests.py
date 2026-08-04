"""
Daily hashing practice checker.

Run all tests:
    python run_all_tests.py

Run one problem:
    python run_all_tests.py subarray-sum-k
    python run_all_tests.py n-queens-style problems by alias below
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    name = path.stem.replace(" ", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
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


def test_frequency_queries() -> tuple[int, int]:
    mod = load_module("hashing1.py")
    tests = [
        ([1, 2, 1, 3, 2, 1], [1, 2, 4], [3, 2, 0]),
        ([5, 5, 5], [5, 1], [3, 0]),
    ]
    passed = 0
    for arr, queries, exp in tests:
        if run_case(f"queries={queries}", mod.query_frequencies(arr, queries), exp):
            passed += 1
    return passed, len(tests)


def test_min_max_frequency() -> tuple[int, int]:
    mod = load_module("hashing2.py")
    tests = [
        ([1, 2, 2, 3, 3, 3], (1, 3)),
        ([4, 4, 4, 4], (4, 4)),
    ]
    passed = 0
    for arr, exp in tests:
        if run_case(str(arr), mod.min_max_frequency_elements(arr), exp):
            passed += 1
    return passed, len(tests)


def test_nearby_duplicate() -> tuple[int, int]:
    mod = load_module("hashing3.py")
    tests = [
        ([1, 2, 3, 1], 3, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]
    passed = 0
    for nums, k, exp in tests:
        if run_case(f"k={k}", mod.contain_nearby_duplicate_hashing(nums, k), exp):
            passed += 1
    return passed, len(tests)


def test_pairs_sum_k() -> tuple[int, int]:
    mod = load_module("hashing4.py")
    tests = [
        ([1, 5, 7, -1, 5], 6, 3),
        ([1, 1, 1], 2, 3),
    ]
    passed = 0
    for arr, k, exp in tests:
        if run_case(f"k={k}", mod.count_with_pairs(arr, k), exp):
            passed += 1
    return passed, len(tests)


def test_pairs_diff_k() -> tuple[int, int]:
    mod = load_module("hashing5.py")
    tests = [
        ([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3], 1, 0),
    ]
    passed = 0
    for arr, k, exp in tests:
        if run_case(f"k={k}", mod.count_with_pairs(arr, k), exp):
            passed += 1
    return passed, len(tests)


def test_pairs_abs_diff_k() -> tuple[int, int]:
    mod = load_module("hashing6.py")
    tests = [
        ([1, 5, 3, 4, 2], 2, 3),
        ([1, 1, 1], 0, 3),
    ]
    passed = 0
    for arr, k, exp in tests:
        if run_case(f"k={k}", mod.count_pairs(arr, k), exp):
            passed += 1
    return passed, len(tests)


def test_prefix_sum() -> tuple[int, int]:
    mod = load_module("hashing7.py")
    nums = [1, 2, 3, 4, 5]
    prefix = mod.build_prefix(nums)
    tests = [((1, 3), 6), ((2, 5), 14)]
    passed = 0
    for (l, r), exp in tests:
        if run_case(f"sum({l},{r})", mod.optimised_sum(prefix, l, r), exp):
            passed += 1
    return passed, len(tests)


def test_subarray_sum_k() -> tuple[int, int]:
    mod = load_module("hashing8.py")
    tests = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
    ]
    passed = 0
    for nums, k, exp in tests:
        if run_case(f"k={k}", mod.optimized_count(nums, k), exp):
            passed += 1
    return passed, len(tests)


def test_longest_subarray_sum_k() -> tuple[int, int]:
    mod = load_module("hashing9.py")
    tests = [
        ([1, -1, 5, -2, 3], 3, (1, 4)),
        ([1, 2, 3], 10, (-1, -1)),
    ]
    passed = 0
    for nums, k, exp in tests:
        if run_case(f"k={k}", mod.largest_subarray_sum_k_optimized(nums, k), exp):
            passed += 1
    return passed, len(tests)


def test_valid_anagram() -> tuple[int, int]:
    mod = load_module("hashing10.py")
    tests = [("anagram", "nagaram", True), ("rat", "car", False)]
    passed = 0
    for s, t, exp in tests:
        if run_case(f"'{s}'", mod.valid_anagram(s, t), exp):
            passed += 1
    return passed, len(tests)


def test_max_subarray() -> tuple[int, int]:
    mod = load_module("hashing11.py")
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1)]
    passed = 0
    for nums, exp in tests:
        if run_case(str(nums[:3]), mod.maximum_subarray_sum_optimized(nums), exp):
            passed += 1
    return passed, len(tests)


def test_max_subarray_v2() -> tuple[int, int]:
    mod = load_module("hashing12.py")
    tests = [([-1], -1), ([-2, -1], -1)]
    passed = 0
    for nums, exp in tests:
        if run_case(str(nums), mod.maximum_subarray_sum_optimized(nums), exp):
            passed += 1
    return passed, len(tests)


def test_minimum_steps() -> tuple[int, int]:
    mod = load_module("hashing13.py")
    tests = [([5, 2, 1], 3), ([1, 1, 1], 0)]
    passed = 0
    for piles, exp in tests:
        if run_case(str(piles), mod.minimum_steps_optimized(piles), exp):
            passed += 1
    return passed, len(tests)


def test_max_distance() -> tuple[int, int]:
    mod = load_module("hashing14.py")
    tests = [([1, 2, 3, 2, 1], 4), ([1, 2, 3, 4], 0)]
    passed = 0
    for arr, exp in tests:
        if run_case(str(arr), mod.max_distance(arr), exp):
            passed += 1
    return passed, len(tests)


def test_first_unique() -> tuple[int, int]:
    mod = load_module("hashing15.py")
    tests = [("leetcode", 0), ("aabb", -1)]
    passed = 0
    for s, exp in tests:
        if run_case(f"'{s}'", mod.first_unique_character(s), exp):
            passed += 1
    return passed, len(tests)


def test_common_characters() -> tuple[int, int]:
    mod = load_module("hashing16.py")
    tests = [
        (["bella", "label", "roller"], sorted(["e", "l", "l"])),
    ]
    passed = 0
    for words, exp in tests:
        got = sorted(mod.common_characters(words))
        if run_case(str(words), got, exp):
            passed += 1
    return passed, len(tests)


def test_longest_consecutive() -> tuple[int, int]:
    mod = load_module("hashing17.py")
    tests = [([100, 4, 200, 1, 3, 2], 4), ([], 0)]
    passed = 0
    for nums, exp in tests:
        if run_case(str(nums[:4]), mod.longest_consecutive_sequence_optimized(nums), exp):
            passed += 1
    return passed, len(tests)


def test_zero_sum_subarray() -> tuple[int, int]:
    mod = load_module("hashing18.py")
    tests = [([15, -2, 2, -8, 1, 7, 10, 23], 5), ([0, 0, 0], 3)]
    passed = 0
    for nums, exp in tests:
        if run_case(str(nums[:4]), mod.max_length_optimized(nums), exp):
            passed += 1
    return passed, len(tests)


def test_count_subarray_k() -> tuple[int, int]:
    mod = load_module("hashing19.py")
    tests = [([10, 2, -2, -20, 10], -10, 3), ([1, 1, 1], 2, 2)]
    passed = 0
    for nums, k, exp in tests:
        if run_case(f"k={k}", mod.count_subarray_optimized(nums, k), exp):
            passed += 1
    return passed, len(tests)


def test_subarray_xor() -> tuple[int, int]:
    mod = load_module("hashing20.py")
    tests = [([4, 2, 2, 6, 4], 6, 4), ([5, 6, 7, 8, 9], 5, 2)]
    passed = 0
    for arr, k, exp in tests:
        if run_case(f"k={k}", mod.subarrays_xor_optimized(arr, k), exp):
            passed += 1
    return passed, len(tests)


def test_good_subarrays() -> tuple[int, int]:
    mod = load_module("hashing21.py")
    tests = [([3, 1, 9, 6], 3, 1), ([1, 2, 3], 2, 2)]
    passed = 0
    for nums, k, exp in tests:
        if run_case(f"k={k}", mod.good_subarrays(nums, k), exp):
            passed += 1
    return passed, len(tests)


def test_stable_subarray() -> tuple[int, int]:
    mod = load_module("hashing22.py")
    tests = [([0, 0], 1), ([1, 2, 1], 0)]
    passed = 0
    for nums, exp in tests:
        if run_case(str(nums), mod.stable_subarray(nums), exp):
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "frequency-queries": test_frequency_queries,
    "min-max-frequency": test_min_max_frequency,
    "nearby-duplicate": test_nearby_duplicate,
    "pairs-sum-k": test_pairs_sum_k,
    "pairs-diff-k": test_pairs_diff_k,
    "pairs-abs-diff-k": test_pairs_abs_diff_k,
    "prefix-sum": test_prefix_sum,
    "subarray-sum-k": test_subarray_sum_k,
    "longest-subarray-sum-k": test_longest_subarray_sum_k,
    "valid-anagram": test_valid_anagram,
    "max-subarray": test_max_subarray,
    "max-subarray-v2": test_max_subarray_v2,
    "minimum-steps": test_minimum_steps,
    "max-distance": test_max_distance,
    "first-unique": test_first_unique,
    "common-characters": test_common_characters,
    "longest-consecutive": test_longest_consecutive,
    "zero-sum-subarray": test_zero_sum_subarray,
    "count-subarray-k": test_count_subarray_k,
    "subarray-xor": test_subarray_xor,
    "good-subarrays": test_good_subarrays,
    "stable-subarray": test_stable_subarray,
}


def main() -> None:
    import sys

    selected = sys.argv[1:] if len(sys.argv) > 1 else list(ALL_TESTS)
    total_passed = 0
    total_cases = 0

    print("=" * 60)
    print("Hashing Daily Tests")
    print("=" * 60)

    for alias in selected:
        if alias not in ALL_TESTS:
            print(f"\nUnknown test: {alias}")
            continue
        print(f"\n{alias}")
        print("-" * len(alias))
        passed, cases = ALL_TESTS[alias]()
        total_passed += passed
        total_cases += cases

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_cases} passed")
    if total_cases and total_passed == total_cases:
        print("All tests passed!")
    elif total_cases:
        print("Some tests failed.")


if __name__ == "__main__":
    main()
