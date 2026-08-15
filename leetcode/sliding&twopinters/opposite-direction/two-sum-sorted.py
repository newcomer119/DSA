# Two Sum Sorted
# Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and with constant auxiliary space.

# Input:

# arr: a sorted integer array
# target: the target sum we want to reach
# Sample Input: [2, 3, 4, 5, 8, 11, 18], 8

# Sample Output: 1 3


def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    l,r = 0, len(arr) - 1
    while l < r:
        two_sum = arr[l] + arr[r]
        if two_sum == target:
            return [l,r]
        elif two_sum  < target:
            l += 1
        else:
            r -= 1

    return []
    # l,r = 0, len(arr) - 1
    # while l < r:
    #     tsum = arr[l] + arr[r]
    #     if tsum == target:
    #         return [l , r]
    #     elif tsum > target:
    #         r -= 1
    #     else:
    #         l += 1

    # return []

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([2, 3, 4, 5, 8, 11, 18], 8, [1, 3]), ([1, 2, 3, 4], 7, [2, 3]), ([1, 2], 3, [0, 1])]
    passed = 0
    for arr, target, exp in TESTS:
        got = two_sum_sorted(arr, target)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
