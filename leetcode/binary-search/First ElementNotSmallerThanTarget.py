# Input:

# arr = [1, 3, 3, 5, 8, 8, 10]
# target = 2
# Output: 1

# Explanation: The first element larger than 2 is 3, which has index 1.

# Input:

# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: 3


def first_not_smaller(arr: list[int], target: int) -> int:
    # l,r = 0,len(arr)-1
    # boundary_index = -1
    # while l <= r:
    #     mid = (l + r) // 2

    #     if arr[mid] >= target:
    #         boundary_index = mid
    #         r = mid - 1
    #     else:
    #         l = mid + 1

    # return boundary_index
    l,r = 0 , len(arr) - 1
    ans= -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            ans = mid
            r = mid - 1

        else :
            l = mid + 1

    return ans

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 3, 3, 5, 8, 8, 10], 2, 1),
        ([2, 3, 5, 7, 11, 13, 17, 19], 6, 3),
        ([1, 2, 3], 10, -1),
        ([5, 7, 9], 5, 0),
        ([1, 3, 5, 7], 7, 3),
    ]
    passed = 0
    for arr, target, expected in TESTS:
        got = first_not_smaller(arr, target)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target}, arr={arr} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")