# Range Sum Query using Prefix Sum
# GFG: https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/
#
# Given an array, answer multiple queries: sum of elements from index l to r (inclusive, 1-based).
#
# Example:
# nums = [1, 2, 3, 4, 5]
# query(1, 3) -> 6
# query(2, 5) -> 14


def brute_force_sum(nums: list[int], l: int, r: int) -> int:
    return sum(nums[l - 1 : r])


def build_prefix(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    return prefix


def optimised_sum(prefix: list[int], l: int, r: int) -> int:
    return prefix[r] - prefix[l - 1]


def range_sum_queries(nums: list[int], queries: list[tuple[int, int]]) -> list[int]:
    prefix = build_prefix(nums)
    return [optimised_sum(prefix, l, r) for l, r in queries]


# --- Daily tests ---
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    TESTS = [
        ((1, 3), 6),
        ((2, 5), 14),
        ((3, 3), 3),
    ]
    prefix = build_prefix(nums)
    passed = 0
    for (l, r), exp in TESTS:
        got = optimised_sum(prefix, l, r)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] sum({l},{r}) -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
