"""
Daily backtracking practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py lc-questions
    python run_all_tests.py dedup

Run one problem:
    python run_all_tests.py subsets
    python run_all_tests.py gray-code
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    name = path.stem.replace(" ", "_").replace("-", "_").replace("&", "and")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def norm_lists(groups):
    return sorted(sorted(g) for g in groups)


def norm_strings(items):
    return sorted(items)


def is_valid_gray_code(seq: list[int], n: int) -> bool:
    expected_len = 1 << n
    if len(seq) != expected_len or len(set(seq)) != expected_len:
        return False
    if seq[0] != 0:
        return False

    def diff_by_one(a: int, b: int) -> bool:
        return (a ^ b).bit_count() == 1

    for i in range(len(seq) - 1):
        if not diff_by_one(seq[i], seq[i + 1]):
            return False
    return diff_by_one(seq[0], seq[-1])


def run_case(name: str, actual, expected) -> bool:
    ok = actual == expected
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         got:      {actual!r}")
    return ok


def build_tree(tokens, node_cls):
    it = iter(tokens)

    def helper():
        val = next(it)
        if val == "x":
            return None
        return node_cls(int(val), helper(), helper())

    return helper()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------------------------------------------
# lc-questions
# ---------------------------------------------------------------------------

def test_restore_ip() -> tuple[int, int]:
    mod = load_module("lc-questions/que1.py")
    sol = mod.Solution()
    tests = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
        ("1111", ["1.1.1.1"]),
    ]
    passed = 0
    for s, expected in tests:
        if run_case(s, norm_strings(sol.restoreIpAddresses(s)), norm_strings(expected)):
            passed += 1
    return passed, len(tests)


def test_path_sum_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que2.py")

    class Solution:
        pathSum = mod.Solution.pathSum

    sol = Solution()
    # tree: 5 / 4,8 / 11,null / 7,2 target 22 -> [5,4,11,2]
    root = build_tree(["5", "4", "11", "7", "x", "x", "2", "x", "x", "x", "x", "8", "x", "x"], TreeNode)
    tests = [
        (root, 22, [[5, 4, 11, 2]]),
        (build_tree(["1", "2", "x", "x", "3", "x", "x"], TreeNode), 5, []),
        (None, 0, []),
    ]
    passed = 0
    for tree, target, expected in tests:
        got = norm_lists(sol.pathSum(tree, target))
        if run_case(f"target={target}", got, norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_beautiful_arrangement() -> tuple[int, int]:
    mod = load_module("lc-questions/que3.py")
    sol = mod.Solution()
    tests = [(1, 1), (2, 2), (3, 3)]
    passed = 0
    for n, expected in tests:
        if run_case(f"n={n}", sol.countArrangement(n), expected):
            passed += 1
    return passed, len(tests)


def test_word_break_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que4.py")
    sol = mod.Solution()
    tests = [
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]),
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
         ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ]
    passed = 0
    for s, words, expected in tests:
        if run_case(s, norm_strings(sol.wordBreak(s, words)), norm_strings(expected)):
            passed += 1
    return passed, len(tests)


def test_nums_same_consec_diff() -> tuple[int, int]:
    mod = load_module("lc-questions/que6.py")
    sol = mod.Solution()
    tests = [
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
        (3, 7, [181, 292, 707, 818, 929]),
        (1, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]
    passed = 0
    for n, k, expected in tests:
        if run_case(f"n={n}, k={k}", sorted(sol.numsSameConsecDiff(n, k)), sorted(expected)):
            passed += 1
    return passed, len(tests)


def test_matchsticks_square() -> tuple[int, int]:
    mod = load_module("lc-questions/que7.py")
    sol = mod.Solution()
    tests = [([1, 1, 2, 2, 2], True), ([3, 3, 3, 3, 4], False), ([1], False), ([1, 1, 1, 1], True)]
    passed = 0
    for sticks, expected in tests:
        if run_case(str(sticks), sol.makesquare(sticks[:]), expected):
            passed += 1
    return passed, len(tests)


def test_permutations_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que8.py")
    sol = mod.Solution()
    tests = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2], [[1, 2], [2, 1]]),
    ]
    passed = 0
    for nums, expected in tests:
        if run_case(str(nums), norm_lists(sol.permuteUnique(nums[:])), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_subsets_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que9.py")
    sol = mod.Solution()
    tests = [
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([0], [[], [0]]),
    ]
    passed = 0
    for nums, expected in tests:
        if run_case(str(nums), norm_lists(sol.subsetsWithDup(nums[:])), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_combination_sum_ii() -> tuple[int, int]:
    mod = load_module("lc-questions/que10.py")
    sol = mod.Solution()
    tests = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([1, 1, 1], 3, [[1, 1, 1]]),
    ]
    passed = 0
    for cands, target, expected in tests:
        if run_case(f"target={target}", norm_lists(sol.combinationSum2(cands[:], target)), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_gray_code() -> tuple[int, int]:
    mod = load_module("lc-questions/que11.py")
    sol = mod.Solution()
    tests = [1, 2, 3]
    passed = 0
    for n in tests:
        got = sol.grayCode(n)
        ok = is_valid_gray_code(got, n)
        if run_case(f"n={n}", ok, True):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# dedup
# ---------------------------------------------------------------------------

def test_subsets() -> tuple[int, int]:
    mod = load_module("dedup/subsets.py")
    tests = [
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([1], [[], [1]]),
        ([], [[]]),
    ]
    passed = 0
    for nums, expected in tests:
        if run_case(str(nums), norm_lists(mod.subsets(nums)), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_combination_sum() -> tuple[int, int]:
    mod = load_module("dedup/combinationsum.py")
    tests = [
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 1, [[1]]),
    ]
    passed = 0
    for cands, target, expected in tests:
        if run_case(f"target={target}", norm_lists(mod.combination_sum(cands, target)), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_three_sum() -> tuple[int, int]:
    mod = load_module("dedup/three_sum.py")
    tests = [
        ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], 0, []),
        ([0, 0, 0], 0, [[0, 0, 0]]),
    ]
    passed = 0
    for nums, target, expected in tests:
        if run_case(f"target={target}", norm_lists(mod.three_sum_unique_triplets(nums[:], target)), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# aggregation&memoization
# ---------------------------------------------------------------------------

def test_coin_change() -> tuple[int, int]:
    mod = load_module("aggregation&memoization/min-coins-to-make-change.py")
    tests = [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([1, 3, 4], 6, 2)]
    passed = 0
    for coins, amount, expected in tests:
        if run_case(f"amount={amount}", mod.coin_change(coins, amount), expected):
            passed += 1
    return passed, len(tests)


def test_decode_ways() -> tuple[int, int]:
    mod = load_module("aggregation&memoization/ways-to-decode-message.py")
    tests = [("12", 2), ("226", 3), ("06", 0), ("11106", 2), ("", 1)]
    passed = 0
    for digits, expected in tests:
        if run_case(digits or "empty", mod.decode_ways(digits), expected):
            passed += 1
    return passed, len(tests)


def test_word_break() -> tuple[int, int]:
    mod = load_module("aggregation&memoization/word-break.py")
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("a", ["a"], True),
    ]
    passed = 0
    for s, words, expected in tests:
        if run_case(s, mod.word_break(s, words), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# additional-states
# ---------------------------------------------------------------------------

def test_permutations() -> tuple[int, int]:
    mod = load_module("additional-states/GeneralAllPermutations.py")
    tests = [("ab", ["ab", "ba"]), ("a", ["a"]), ("xyz", ["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"])]
    passed = 0
    for letters, expected in tests:
        if run_case(letters, norm_strings(mod.permutations(letters)), norm_strings(expected)):
            passed += 1
    return passed, len(tests)


def test_generate_parentheses() -> tuple[int, int]:
    mod = load_module("additional-states/valid_parentheses.py")
    tests = [(1, ["()"]), (2, ["(())", "()()"]), (3, None)]
    passed = 0
    for n, expected in tests:
        got = norm_strings(mod.generate_parentheses(n))
        if expected is None:
            ok = len(got) == 5  # catalan C3 = 5
            name = f"n={n} count"
            exp_display = 5
            got_display = len(got)
        else:
            ok = got == norm_strings(expected)
            name = f"n={n}"
            exp_display = expected
            got_display = got
        if run_case(name, got_display if expected is None else got, exp_display if expected is None else norm_strings(expected)):
            passed += int(ok)
    return passed, len(tests)


# ---------------------------------------------------------------------------
# pruning
# ---------------------------------------------------------------------------

def test_palindrome_partition() -> tuple[int, int]:
    mod = load_module("pruining/string_palindrome_partition.py")
    tests = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ]
    passed = 0
    for s, expected in tests:
        if run_case(s, norm_lists(mod.partition(s)), norm_lists(expected)):
            passed += 1
    return passed, len(tests)


def test_n_queens() -> tuple[int, int]:
    mod = load_module("pruining/n-queens.py")
    tests = [
        (1, [["Q"]]),
        (2, []),
        (4, [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]),
    ]
    passed = 0
    for n, expected in tests:
        got = sorted(mod.solve_n_queens(n))
        exp = sorted(expected)
        if run_case(f"n={n}", got, exp):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# combination-search
# ---------------------------------------------------------------------------

def test_phone_letter_combinations() -> tuple[int, int]:
    mod = load_module("combination-search/letter_combinations_of_phone_number.py")
    tests = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]
    passed = 0
    for digits, expected in tests:
        if run_case(digits or "empty", norm_strings(mod.letter_combinations_of_phone_number(digits)), norm_strings(expected)):
            passed += 1
    return passed, len(tests)


def test_letter_combination() -> tuple[int, int]:
    mod = load_module("combination-search/letter_combination.py")
    tests = [(1, ["a", "b"]), (2, ["aa", "ab", "ba", "bb"]), (0, [])]
    passed = 0
    for n, expected in tests:
        got = mod.letter_combination(n) if n > 0 else []
        if run_case(f"n={n}", norm_strings(got), norm_strings(expected)):
            passed += 1
    return passed, len(tests)


def test_ternary_paths() -> tuple[int, int]:
    mod = load_module("combination-search/ternary_path.py")
    root = mod.Node(1, [mod.Node(2), mod.Node(3), mod.Node(4)])
    root2 = mod.Node(1, [mod.Node(2, [mod.Node(5)])])
    tests = [
        (root, sorted(["1->2", "1->3", "1->4"])),
        (root2, sorted(["1->2->5"])),
    ]
    passed = 0
    for tree, expected in tests:
        got = sorted(mod.ternary_tree_paths(tree))
        if run_case("paths", got, expected):
            passed += 1
    return passed, len(tests)


ALL_TESTS = {
    "restore-ip": ("lc-questions", test_restore_ip),
    "path-sum-ii": ("lc-questions", test_path_sum_ii),
    "beautiful-arrangement": ("lc-questions", test_beautiful_arrangement),
    "word-break-ii": ("lc-questions", test_word_break_ii),
    "consec-diff": ("lc-questions", test_nums_same_consec_diff),
    "matchsticks-square": ("lc-questions", test_matchsticks_square),
    "permutations-ii": ("lc-questions", test_permutations_ii),
    "subsets-ii": ("lc-questions", test_subsets_ii),
    "combination-sum-ii": ("lc-questions", test_combination_sum_ii),
    "gray-code": ("lc-questions", test_gray_code),
    "subsets": ("dedup", test_subsets),
    "combination-sum": ("dedup", test_combination_sum),
    "three-sum": ("dedup", test_three_sum),
    "coin-change": ("aggregation&memoization", test_coin_change),
    "decode-ways": ("aggregation&memoization", test_decode_ways),
    "word-break": ("aggregation&memoization", test_word_break),
    "permutations": ("additional-states", test_permutations),
    "generate-parentheses": ("additional-states", test_generate_parentheses),
    "palindrome-partition": ("pruining", test_palindrome_partition),
    "n-queens": ("pruining", test_n_queens),
    "phone-letters": ("combination-search", test_phone_letter_combinations),
    "letter-combination": ("combination-search", test_letter_combination),
    "ternary-paths": ("combination-search", test_ternary_paths),
}


def main() -> int:
    filters = [a.lower() for a in sys.argv[1:]]

    if filters:
        selected = {k: v for k, v in ALL_TESTS.items() if any(f in k or f in v[0] for f in filters)}
        if not selected:
            print("No matching problems. Available:")
            for key, (folder, _) in ALL_TESTS.items():
                print(f"  - {key} ({folder})")
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed = []
    current_folder = None

    print("=" * 60)
    print("Backtracking Daily Tests")
    print("=" * 60)

    for key, (folder, runner) in selected.items():
        if folder != current_folder:
            print(f"\n[{folder}]")
            current_folder = folder
        print(f"\n{key}")
        print("-" * len(key))
        passed, count = runner()
        total_passed += passed
        total_cases += count
        if passed != count:
            failed.append(key)

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_cases} passed")
    if failed:
        print("Needs review:", ", ".join(failed))
        return 1
    print("All tests passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
