# A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array.

# Input: [30, 40, 50, 10, 20]

# Output: 3

# Explanation: The smallest element is 10, and its index is 3.

# Input: [3, 5, 7, 11, 13, 17, 19, 2]

# Output: 7

# Explanation: The smallest element is 2, and its index is 7.


def find_min_rotated(arr: list[int]) -> int:
    left,right = 0 , len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([30, 40, 50, 10, 20], 3),
        ([3, 5, 7, 11, 13, 17, 19, 2], 7),
        ([1, 2, 3, 4, 5], 0),
        ([2, 1], 1),
        ([1, 2], 0),
    ]
    passed = 0
    for arr, expected in TESTS:
        got = find_min_rotated(arr)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {arr} -> index {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")