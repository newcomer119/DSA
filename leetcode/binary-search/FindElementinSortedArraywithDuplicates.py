# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

# Input:

# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1

# Explanation: The first occurrence of 3 is at index 1.

# Input:

# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1

# Explanation: 6 does not exist in the array.


def find_first_occurrence(arr: list[int], target: int) -> int:
    # l,r = 0, len(arr) - 1
    # ans = -1
    # while l<=r:
    #     mid = (l + r) // 2
    #     if arr[mid] == target:
    #         ans = mid
    #         r = mid - 1
    #     elif arr[mid] < target:
    #         l = mid + 1

    #     else:
    #         r= mid - 1

    # return ans


    left , right = 0 ,len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans 


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3, 1),
        ([2, 3, 5, 7, 11, 13, 17, 19], 6, -1),
        ([7], 7, 0),
        ([7], 3, -1),
        ([1, 2, 2, 2, 9], 9, 4),
    ]
    passed = 0
    for arr, target, expected in TESTS:
        got = find_first_occurrence(arr, target)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")