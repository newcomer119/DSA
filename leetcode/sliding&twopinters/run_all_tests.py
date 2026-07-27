"""
Daily sliding window & two pointers practice checker.

Run all tests:
    python run_all_tests.py

Run one subfolder:
    python run_all_tests.py sliding-window
    python run_all_tests.py leetcode

Run one problem:
    python run_all_tests.py koko
    python run_all_tests.py container
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(relative_path: str):
    path = ROOT / relative_path
    name = path.stem.replace(" ", "_").replace("-", "_").replace("&", "and")
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


def build_list(values, node_cls):
    if not values:
        return None
    head = node_cls(values[0])
    cur = head
    for val in values[1:]:
        cur.next = node_cls(val)
        cur = cur.next
    return head


def list_from_head(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build_cyclic_list(values, cycle_pos, node_cls):
    if not values:
        return None
    nodes = [node_cls(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


# ---------------------------------------------------------------------------
# leetcode-questions
# ---------------------------------------------------------------------------

def test_que1_reverse_vowels() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que1.py")

    class Solution:
        reverseVowels = mod.reverseVowels

    sol = Solution()
    tests = [
        ("example 1", "IceCreAm", "AceCreIm"),
        ("example 2", "leetcode", "leotcede"),
        ("no vowels", "bcdfg", "bcdfg"),
        ("all vowels", "aeiou", "uoiea"),
        ("single char", "a", "a"),
    ]
    passed = 0
    for name, s, expected in tests:
        if run_case(name, sol.reverseVowels(s), expected):
            passed += 1
    return passed, len(tests)


def test_que2_valid_palindrome_ii() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que2.py")
    sol = mod.Solution()
    tests = [
        ("example 1", "aba", True),
        ("example 2", "abca", True),
        ("example 3", "abc", False),
        ("already palindrome", "racecar", True),
        ("two deletes needed", "abcdef", False),
    ]
    passed = 0
    for name, s, expected in tests:
        if run_case(name, sol.validPalindrome(s), expected):
            passed += 1
    return passed, len(tests)


def test_que3_compress() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que3.py")
    sol = mod.Solution()
    tests = [
        (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
        (["a"], 1, ["a"]),
        (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4, ["a", "b", "1", "2"]),
        (["a", "a", "a", "b", "b", "a", "a"], 6, ["a", "3", "b", "2", "a", "2"]),
    ]
    passed = 0
    for chars, expected_len, expected_prefix in tests:
        data = chars[:]
        got_len = sol.compress(data)
        ok = got_len == expected_len and data[:expected_len] == expected_prefix
        print(f"  [{'PASS' if ok else 'FAIL'}] compress -> len {got_len}, prefix {data[:got_len]}")
        if not ok:
            print(f"         expected len {expected_len}, prefix {expected_prefix}")
        passed += int(ok)
    return passed, len(tests)


def test_que4_max_area() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que4.py")
    sol = mod.Solution()
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]
    passed = 0
    for height, expected in tests:
        if run_case(str(height), sol.maxArea(height), expected):
            passed += 1
    return passed, len(tests)


def test_que5_rescue_boats() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que5.py")

    class Solution:
        numRescueBoats = mod.numRescueBoats

    sol = Solution()
    tests = [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        ([1, 1, 1, 1], 2, 2),
    ]
    passed = 0
    for people, limit, expected in tests:
        if run_case(f"people={people}, limit={limit}", sol.numRescueBoats(people[:], limit), expected):
            passed += 1
    return passed, len(tests)


def test_que6_three_sum() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que6.py")

    class Solution:
        threeSum = mod.threeSum

    sol = Solution()

    def normalize(groups):
        return sorted(sorted(g) for g in groups)

    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]
    passed = 0
    for nums, expected in tests:
        got = normalize(sol.threeSum(nums[:]))
        exp = normalize(expected)
        if run_case(str(nums), got, exp):
            passed += 1
    return passed, len(tests)


def test_que7_two_distinct() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que7.py")

    class Solution:
        lengthOfLongestSubstringTwoDistinct = mod.lengthOfLongestSubstringTwoDistinct

    sol = Solution()
    tests = [
        ("eceba", 3),
        ("ccaabbb", 5),
        ("a", 1),
        ("abac", 3),
    ]
    passed = 0
    for s, expected in tests:
        if run_case(s, sol.lengthOfLongestSubstringTwoDistinct(s), expected):
            passed += 1
    return passed, len(tests)


def test_que8_min_swaps() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que8.py")

    class Solution:
        minSwaps = mod.minSwaps

    sol = Solution()
    tests = [
        ([1, 0, 1, 0, 1], 1),
        ([0, 0, 0, 1, 0], 0),
        ([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1], 3),
        ([1, 1, 1], 0),
    ]
    passed = 0
    for data, expected in tests:
        if run_case(str(data), sol.minSwaps(data), expected):
            passed += 1
    return passed, len(tests)


def test_que9_min_subarray_len() -> tuple[int, int]:
    mod = load_module("leetcode-questions/que9.py")

    class Solution:
        minSubArrayLen = mod.minSubArrayLen

    sol = Solution()
    tests = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
    ]
    passed = 0
    for target, nums, expected in tests:
        if run_case(f"target={target}", sol.minSubArrayLen(target, nums), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# cycle-and-advanced
# ---------------------------------------------------------------------------

def test_teleporter() -> tuple[int, int]:
    mod = load_module("cycle-and-advanced.py/Teleporter-Arrays.py")
    tests = [
        ([2, 4, 5, 8, 10], [4, 6, 8, 9], 30),
        ([1, 3, 5], [2, 4, 6], 12),
        ([1], [1], 1),
        ([1, 2, 3], [4, 5, 6], 15),
    ]
    passed = 0
    for a1, a2, expected in tests:
        if run_case(f"arr1={a1}, arr2={a2}", mod.maximum_score(a1, a2), expected):
            passed += 1
    return passed, len(tests)


def test_minimum_window() -> tuple[int, int]:
    mod = load_module("cycle-and-advanced.py/minimum-window.py")
    tests = [
        ("cdbaebaecd", "abc", "baec"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
    ]
    passed = 0
    for original, check, expected in tests:
        if run_case(f"{original}/{check}", mod.get_minimum_window(original, check), expected):
            passed += 1
    return passed, len(tests)


def test_linked_list_cycle() -> tuple[int, int]:
    mod = load_module("cycle-and-advanced.py/linked-list.py")
    passed = 0
    total = 3

    no_cycle = build_list([1, 2, 3, 4], mod.Node)
    if run_case("no cycle", mod.has_cycle(no_cycle), False):
        passed += 1

    cycle = build_cyclic_list([1, 2, 3, 4], 1, mod.Node)
    if run_case("cycle exists", mod.has_cycle(cycle), True):
        passed += 1

    single = mod.Node(1)
    if run_case("single node", mod.has_cycle(single), False):
        passed += 1

    return passed, total


# ---------------------------------------------------------------------------
# prefix-sum
# ---------------------------------------------------------------------------

def test_product_of_array() -> tuple[int, int]:
    mod = load_module("prefix-sum/product-of-array.py")
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 1], [1, 1]),
        ([5], [1]),
    ]
    passed = 0
    for nums, expected in tests:
        if run_case(str(nums), mod.product_of_array_except_self(nums), expected):
            passed += 1
    return passed, len(tests)


def test_range_sum_query() -> tuple[int, int]:
    mod = load_module("prefix-sum/range-sum-query.py")
    tests = [
        ([1, 2, 3, 4], 1, 3, 9),
        ([1, 2, 3, 4], 0, 0, 1),
        ([1, 2, 3, 4], 0, 3, 10),
        ([5, 5, 5], 1, 2, 10),
    ]
    passed = 0
    for nums, left, right, expected in tests:
        if run_case(f"sum({left},{right})", mod.range_sum_query_immutable(nums, left, right), expected):
            passed += 1
    return passed, len(tests)


def test_subarray_sum_equals() -> tuple[int, int]:
    mod = load_module("prefix-sum/subarray-sum-equals-target.py")
    tests = [
        ([1, -20, -3, 30, 5, 4], 7, [1, 4]),
        ([1, 2, 3], 5, [1, 3]),
        ([1, 2, 3], 10, []),
        ([0, 0, 0], 0, [0, 1]),
    ]
    passed = 0
    for nums, target, expected in tests:
        if run_case(f"target={target}", mod.subarray_sum(nums, target), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# sliding-window
# ---------------------------------------------------------------------------

def test_least_consec_cards() -> tuple[int, int]:
    mod = load_module("sliding-window/least-consec-cards-to-match.py")
    tests = [
        ([3, 4, 2, 3, 4, 7], 4),
        ([1, 2, 3, 4], -1),
        ([1, 1], 2),
        ([5, 5, 5, 5], 2),
    ]
    passed = 0
    for cards, expected in tests:
        if run_case(str(cards), mod.least_consecutive_cards_to_match(cards), expected):
            passed += 1
    return passed, len(tests)


def test_subarray_sum_shortest() -> tuple[int, int]:
    mod = load_module("sliding-window/subarray-sum-shortest.py")
    tests = [
        ([1, 4, 1, 7, 3, 0, 2, 5], 10, 2),
        ([2, 3, 1, 2, 4, 3], 7, 2),
        ([1, 1, 1, 1], 10, 0),
        ([4, 2, 1, 1], 6, 2),
    ]
    passed = 0
    for nums, target, expected in tests:
        if run_case(f"target={target}", mod.subarray_sum_shortest(nums, target), expected):
            passed += 1
    return passed, len(tests)


def test_longest_substring() -> tuple[int, int]:
    mod = load_module("sliding-window/longest-substring-without-repeating.py")
    tests = [
        ("abccabcabcc", 3),
        ("aaaabaaa", 2),
        ("abcabcbb", 3),
        ("", 0),
        ("a", 1),
    ]
    passed = 0
    for s, expected in tests:
        if run_case(repr(s), mod.longest_substring_without_repeating_characters(s), expected):
            passed += 1
    return passed, len(tests)


def test_subarray_sum_longest() -> tuple[int, int]:
    mod = load_module("sliding-window/subarray-sum-longest.py")
    tests = [
        ([1, 6, 3, 1, 2, 4, 5], 10, 4),
        ([1, 2, 3], 6, 3),
        ([5, 1, 1, 1], 5, 3),
        ([1, 1, 1, 1], 3, 3),
    ]
    passed = 0
    for nums, target, expected in tests:
        if run_case(f"target={target}", mod.subarray_sum_longest(nums, target), expected):
            passed += 1
    return passed, len(tests)


def test_find_all_anagrams() -> tuple[int, int]:
    mod = load_module("sliding-window/find-all-anagrams-in-a-string.py")
    tests = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aaaa", "aa", [0, 1, 2]),
        ("a", "aa", []),
    ]
    passed = 0
    for original, check, expected in tests:
        if run_case(f"{original}/{check}", mod.find_all_anagrams(original, check), expected):
            passed += 1
    return passed, len(tests)


def test_subarray_sum_fixed() -> tuple[int, int]:
    mod = load_module("sliding-window/subarray-sum-fixed.py")
    tests = [
        ([1, 2, 3, 7, 4, 1], 3, 14),
        ([1, 1, 1, 1], 2, 2),
        ([5], 1, 5),
        ([1, 2, 3, 4, 5], 3, 12),
    ]
    passed = 0
    for nums, k, expected in tests:
        if run_case(f"k={k}", mod.subarray_sum_fixed(nums, k), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# opposite-direction
# ---------------------------------------------------------------------------

def test_container_water() -> tuple[int, int]:
    mod = load_module("opposite-direction/container-most-water.py")
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
    ]
    passed = 0
    for arr, expected in tests:
        if run_case(str(arr), mod.container_with_most_water(arr), expected):
            passed += 1
    return passed, len(tests)


def test_valid_palindrome() -> tuple[int, int]:
    mod = load_module("opposite-direction/valid-palindrome.py")
    tests = [
        ("Do geese see God?", True),
        ("Was it a car or a cat I saw?", True),
        ("A brown fox jumping over", False),
        (" ", True),
        ("0P", False),
    ]
    passed = 0
    for s, expected in tests:
        if run_case(repr(s), mod.is_palindrome(s), expected):
            passed += 1
    return passed, len(tests)


def test_two_sum_sorted() -> tuple[int, int]:
    mod = load_module("opposite-direction/two-sum-sorted.py")
    tests = [
        ([2, 3, 4, 5, 8, 11, 18], 8, [1, 3]),
        ([1, 2, 3, 4], 7, [2, 3]),
        ([1, 2], 3, [0, 1]),
    ]
    passed = 0
    for arr, target, expected in tests:
        if run_case(f"target={target}", mod.two_sum_sorted(arr, target), expected):
            passed += 1
    return passed, len(tests)


# ---------------------------------------------------------------------------
# same-direction
# ---------------------------------------------------------------------------

def test_remove_nth_from_end() -> tuple[int, int]:
    mod = load_module("same-direction/RemoveN-thNode.py")
    tests = [
        ([1, 2, 3, 4], 1, [1, 2, 3]),
        ([1, 2, 3, 4], 2, [1, 2, 4]),
        ([1, 2, 3, 4], 4, [2, 3, 4]),
        ([1], 1, []),
    ]
    passed = 0
    for values, n, expected in tests:
        head = build_list(values, mod.Node)
        got = list_from_head(mod.remove_nth_from_end(head, n))
        if run_case(f"list={values}, n={n}", got, expected):
            passed += 1
    return passed, len(tests)


def test_move_zeros() -> tuple[int, int]:
    mod = load_module("same-direction/Move-Zeros.py")
    tests = [
        ([1, 0, 2, 0, 0, 7], [1, 2, 7, 0, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0], [0]),
    ]
    passed = 0
    for nums, expected in tests:
        data = nums[:]
        mod.move_zeros(data)
        if run_case(str(nums), data, expected):
            passed += 1
    return passed, len(tests)


def test_middle_linked_list() -> tuple[int, int]:
    mod = load_module("same-direction/middle-linked-list.py")
    tests = [
        ([0, 1, 2, 3, 4], 2),
        ([0, 1, 2, 3, 4, 5], 3),
        ([1], 1),
        ([1, 2], 2),
    ]
    passed = 0
    for values, expected in tests:
        head = build_list(values, mod.Node)
        if run_case(str(values), mod.middle_of_linked_list(head), expected):
            passed += 1
    return passed, len(tests)


def test_remove_duplicates() -> tuple[int, int]:
    mod = load_module("same-direction/dups.py")
    tests = [
        ([0, 0, 1, 1, 1, 2, 2], 3, [0, 1, 2]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]
    passed = 0
    for arr, expected_len, expected_prefix in tests:
        data = arr[:]
        got_len = mod.remove_duplicates(data)
        ok = got_len == expected_len and data[:expected_len] == expected_prefix
        print(f"  [{'PASS' if ok else 'FAIL'}] {arr} -> len {got_len}, prefix {data[:got_len]}")
        passed += int(ok)
    return passed, len(tests)


ALL_TESTS = {
    # leetcode-questions
    "reverse-vowels": ("leetcode-questions", test_que1_reverse_vowels),
    "valid-palindrome-ii": ("leetcode-questions", test_que2_valid_palindrome_ii),
    "compress-chars": ("leetcode-questions", test_que3_compress),
    "max-area": ("leetcode-questions", test_que4_max_area),
    "rescue-boats": ("leetcode-questions", test_que5_rescue_boats),
    "three-sum": ("leetcode-questions", test_que6_three_sum),
    "two-distinct": ("leetcode-questions", test_que7_two_distinct),
    "min-swaps": ("leetcode-questions", test_que8_min_swaps),
    "min-subarray-len": ("leetcode-questions", test_que9_min_subarray_len),
    # cycle-and-advanced
    "teleporter": ("cycle-and-advanced", test_teleporter),
    "minimum-window": ("cycle-and-advanced", test_minimum_window),
    "linked-list-cycle": ("cycle-and-advanced", test_linked_list_cycle),
    # prefix-sum
    "product-of-array": ("prefix-sum", test_product_of_array),
    "range-sum-query": ("prefix-sum", test_range_sum_query),
    "subarray-sum-equals": ("prefix-sum", test_subarray_sum_equals),
    # sliding-window
    "least-consec-cards": ("sliding-window", test_least_consec_cards),
    "subarray-sum-shortest": ("sliding-window", test_subarray_sum_shortest),
    "longest-substring": ("sliding-window", test_longest_substring),
    "subarray-sum-longest": ("sliding-window", test_subarray_sum_longest),
    "find-all-anagrams": ("sliding-window", test_find_all_anagrams),
    "subarray-sum-fixed": ("sliding-window", test_subarray_sum_fixed),
    # opposite-direction
    "container": ("opposite-direction", test_container_water),
    "valid-palindrome": ("opposite-direction", test_valid_palindrome),
    "two-sum-sorted": ("opposite-direction", test_two_sum_sorted),
    # same-direction
    "remove-nth-node": ("same-direction", test_remove_nth_from_end),
    "move-zeros": ("same-direction", test_move_zeros),
    "middle-linked-list": ("same-direction", test_middle_linked_list),
    "remove-duplicates": ("same-direction", test_remove_duplicates),
}


def main() -> int:
    import sys

    filters = [a.lower() for a in sys.argv[1:]]

    if filters:
        selected = {
            k: v
            for k, v in ALL_TESTS.items()
            if any(f in k or f in v[0] for f in filters)
        }
        if not selected:
            print("No matching problems. Try:")
            for key, (folder, _) in ALL_TESTS.items():
                print(f"  - {key}  ({folder})")
            return 1
    else:
        selected = ALL_TESTS

    total_passed = 0
    total_cases = 0
    failed = []
    current_folder = None

    print("=" * 60)
    print("Sliding Window & Two Pointers Daily Tests")
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
