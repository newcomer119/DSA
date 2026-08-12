"""
Daily dynamic programming practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py 1-d
    python run_all_tests.py 2-d

Run one problem:
    python run_all_tests.py coin-change
    python run_all_tests.py lis
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    name = path.stem.replace(" ", "_").replace("-", "_").replace(",", "_")
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


# ---------------------------------------------------------------------------
# 1-d
# ---------------------------------------------------------------------------

def test_climbing_stairs() -> tuple[int, int]:
    mod = load_module("1-d/climbing-stairs.py")
    tests = [(1, 1), (2, 2), (5, 8)]
    passed = sum(run_case(f"n={n}", mod.climb_stairs(n), exp) for n, exp in tests)
    return passed, len(tests)


def test_house_robber() -> tuple[int, int]:
    mod = load_module("1-d/house-robber.py")
    tests = [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12)]
    passed = sum(run_case(str(nums), mod.rob(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_house_robber_ii() -> tuple[int, int]:
    mod = load_module("1-d/house-robber-II.py")
    tests = [([2, 3, 2], 3), ([1, 2, 3, 1], 4)]
    passed = sum(run_case(str(nums), mod.rob_circular(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_min_cost_climbing() -> tuple[int, int]:
    mod = load_module("1-d/min-cost-climbing.py")
    tests = [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)]
    passed = sum(run_case(str(cost[:3]), mod.min_cost_climbing_stairs(cost), exp) for cost, exp in tests)
    return passed, len(tests)


def test_min_cost_tickets() -> tuple[int, int]:
    mod = load_module("1-d/min-cost-tickets.py")
    tests = [([1, 4, 6, 7, 8, 20], [2, 7, 15], 11)]
    passed = sum(run_case("travel plan", mod.mincost_tickets(days, costs), exp) for days, costs, exp in tests)
    return passed, len(tests)


def test_tribonacci() -> tuple[int, int]:
    mod = load_module("1-d/nth-tribonaaci.py")
    tests = [(0, 0), (4, 4), (25, 1389537)]
    passed = sum(run_case(f"n={n}", mod.tribonacci(n), exp) for n, exp in tests)
    return passed, len(tests)


# ---------------------------------------------------------------------------
# 2-d
# ---------------------------------------------------------------------------

def test_coin_change() -> tuple[int, int]:
    mod = load_module("2-d/coin-change.py")
    tests = [([1, 2, 5], 11, 3), ([2], 3, -1)]
    passed = sum(run_case(f"amount={a}", mod.coin_change(coins, a), exp) for coins, a, exp in tests)
    return passed, len(tests)


def test_coin_change_ii() -> tuple[int, int]:
    mod = load_module("2-d/coin-change2.py")
    tests = [(5, [1, 2, 5], 4), (3, [2], 0)]
    passed = sum(run_case(f"amount={a}", mod.coin_change_ii(a, coins), exp) for a, coins, exp in tests)
    return passed, len(tests)


def test_unique_paths() -> tuple[int, int]:
    mod = load_module("2-d/unique-paths.py")
    tests = [(3, 7, 28), (3, 2, 3)]
    passed = sum(run_case(f"{m}x{n}", mod.unique_paths(m, n), exp) for m, n, exp in tests)
    return passed, len(tests)


def test_unique_paths_ii() -> tuple[int, int]:
    mod = load_module("2-d/unique2.py")
    tests = [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2)]
    passed = sum(run_case("obstacles", mod.unique_paths_with_obstacles(grid), exp) for grid, exp in tests)
    return passed, len(tests)


def test_min_path_sum() -> tuple[int, int]:
    mod = load_module("2-d/minimum-path-sum.py")
    tests = [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)]
    passed = sum(run_case("grid", mod.min_path_sum(grid), exp) for grid, exp in tests)
    return passed, len(tests)


def test_lcs() -> tuple[int, int]:
    mod = load_module("2-d/lcs.py")
    tests = [("abcde", "ace", 3), ("abc", "def", 0)]
    passed = sum(run_case(f"'{t1}'", mod.longest_common_subsequence(t1, t2), exp) for t1, t2, exp in tests)
    return passed, len(tests)


def test_edit_distance() -> tuple[int, int]:
    mod = load_module("2-d/edit-distance.py")
    tests = [("horse", "ros", 3), ("intention", "execution", 5)]
    passed = sum(run_case(f"'{w1}'", mod.min_distance(w1, w2), exp) for w1, w2, exp in tests)
    return passed, len(tests)


def test_distinct_subsequences() -> tuple[int, int]:
    mod = load_module("2-d/distinct-subsequences.py")
    tests = [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5)]
    passed = sum(run_case("distinct", mod.num_distinct(s, t), exp) for s, t, exp in tests)
    return passed, len(tests)


def test_interleaving() -> tuple[int, int]:
    mod = load_module("2-d/interleaving-strings.py")
    tests = [("aabcc", "dbbca", "aadbbcbcac", True), ("aabcc", "dbbca", "aadbbbaccc", False)]
    passed = sum(run_case("interleave", mod.is_interleave(s1, s2, s3), exp) for s1, s2, s3, exp in tests)
    return passed, len(tests)


def test_decode_ways() -> tuple[int, int]:
    mod = load_module("2-d/decode-waysdp.py")
    tests = [("12", 2), ("226", 3), ("06", 0)]
    passed = sum(run_case(f"'{d}'", mod.num_decodings(d), exp) for d, exp in tests)
    return passed, len(tests)


def test_word_break() -> tuple[int, int]:
    mod = load_module("2-d/wordDict.py")
    tests = [("leetcode", ["leet", "code"], True), ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)]
    passed = sum(run_case(f"'{s}'", mod.word_break(s, words), exp) for s, words, exp in tests)
    return passed, len(tests)


def test_partition() -> tuple[int, int]:
    mod = load_module("2-d/partition-equal-subsetsum.py")
    tests = [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)]
    passed = sum(run_case(str(nums), mod.can_partition(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_target_sum() -> tuple[int, int]:
    mod = load_module("2-d/target-sum.py")
    tests = [([1, 1, 1, 1, 1], 3, 5), ([1], 1, 1)]
    passed = sum(run_case("target=3", mod.find_target_sum_ways(nums, target), exp) for nums, target, exp in tests)
    return passed, len(tests)


def test_lis() -> tuple[int, int]:
    mod = load_module("2-d/lis.py")
    tests = [([10, 9, 2, 5, 3, 7, 101, 18], 4), ([7, 7, 7, 7], 1)]
    passed = sum(run_case("lis", mod.length_of_lis(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_longest_palindrome() -> tuple[int, int]:
    mod = load_module("2-d/longest-palindromic.py")
    tests = [("babad", {"bab", "aba"}), ("cbbd", {"bb"})]
    passed = 0
    for s, exp_set in tests:
        if run_case(f"'{s}'", mod.longest_palindrome(s) in exp_set, True):
            passed += 1
    return passed, len(tests)


def test_count_palindromes() -> tuple[int, int]:
    mod = load_module("2-d/count-palindromic-substring.py")
    tests = [("abc", 3), ("aaa", 6)]
    passed = sum(run_case(f"'{s}'", mod.count_substrings(s), exp) for s, exp in tests)
    return passed, len(tests)


def test_lip_matrix() -> tuple[int, int]:
    mod = load_module("2-d/longest-increasing-pathmatrix.py")
    tests = [([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4), ([[1]], 1)]
    passed = sum(run_case("matrix", mod.longest_increasing_path(matrix), exp) for matrix, exp in tests)
    return passed, len(tests)


def test_regex() -> tuple[int, int]:
    mod = load_module("2-d/regular-expression.py")
    tests = [("aa", "a", False), ("aa", "a*", True), ("ab", ".*", True)]
    passed = sum(run_case(f"'{s}'~'{p}'", mod.is_match(s, p), exp) for s, p, exp in tests)
    return passed, len(tests)


def test_burst_balloons() -> tuple[int, int]:
    mod = load_module("2-d/burst-balloons.py")
    tests = [([3, 1, 5, 8], 167), ([1, 5], 10)]
    passed = sum(run_case(str(nums), mod.max_coins(nums), exp) for nums, exp in tests)
    return passed, len(tests)


def test_stock_cooldown() -> tuple[int, int]:
    mod = load_module("2-d/buy-stocks-cooldown.py")
    tests = [([1, 2, 3, 0, 2], 3), ([1], 0)]
    passed = sum(run_case(str(prices), mod.max_profit_cooldown(prices), exp) for prices, exp in tests)
    return passed, len(tests)


def test_max_product() -> tuple[int, int]:
    mod = load_module("2-d/maximum-product-subarray.py")
    tests = [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)]
    passed = sum(run_case(str(nums), mod.max_product(nums), exp) for nums, exp in tests)
    return passed, len(tests)


ALL_TESTS = {
    "climbing-stairs": ("1-d", test_climbing_stairs),
    "house-robber": ("1-d", test_house_robber),
    "house-robber-ii": ("1-d", test_house_robber_ii),
    "min-cost-climbing": ("1-d", test_min_cost_climbing),
    "min-cost-tickets": ("1-d", test_min_cost_tickets),
    "tribonacci": ("1-d", test_tribonacci),
    "coin-change": ("2-d", test_coin_change),
    "coin-change-ii": ("2-d", test_coin_change_ii),
    "unique-paths": ("2-d", test_unique_paths),
    "unique-paths-ii": ("2-d", test_unique_paths_ii),
    "min-path-sum": ("2-d", test_min_path_sum),
    "lcs": ("2-d", test_lcs),
    "edit-distance": ("2-d", test_edit_distance),
    "distinct-subsequences": ("2-d", test_distinct_subsequences),
    "interleaving": ("2-d", test_interleaving),
    "decode-ways": ("2-d", test_decode_ways),
    "word-break": ("2-d", test_word_break),
    "partition": ("2-d", test_partition),
    "target-sum": ("2-d", test_target_sum),
    "lis": ("2-d", test_lis),
    "longest-palindrome": ("2-d", test_longest_palindrome),
    "count-palindromes": ("2-d", test_count_palindromes),
    "lip-matrix": ("2-d", test_lip_matrix),
    "regex": ("2-d", test_regex),
    "burst-balloons": ("2-d", test_burst_balloons),
    "stock-cooldown": ("2-d", test_stock_cooldown),
    "max-product": ("2-d", test_max_product),
}


def main() -> None:
    selected = sys.argv[1:] if len(sys.argv) > 1 else list(ALL_TESTS)
    total_passed = 0
    total_cases = 0
    current_folder = None

    print("=" * 60)
    print("Dynamic Programming Daily Tests")
    print("=" * 60)

    for alias in selected:
        if alias in ("1-d", "2-d"):
            for name, (folder, fn) in ALL_TESTS.items():
                if folder == alias:
                    if current_folder != folder:
                        current_folder = folder
                        print(f"\n[{folder}]")
                    print(f"\n{name}")
                    print("-" * len(name))
                    passed, cases = fn()
                    total_passed += passed
                    total_cases += cases
            continue

        if alias not in ALL_TESTS:
            print(f"\nUnknown test: {alias}")
            continue

        folder, fn = ALL_TESTS[alias]
        if current_folder != folder:
            current_folder = folder
            print(f"\n[{folder}]")
        print(f"\n{alias}")
        print("-" * len(alias))
        passed, cases = fn()
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
