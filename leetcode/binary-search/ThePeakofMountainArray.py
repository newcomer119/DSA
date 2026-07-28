# A mountain array is defined as an array that

# has at least 3 elements
# has an element with the largest value called "peak", with index k. The array elements strictly increase from the first element to A[k], and then strictly decrease from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.
# That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is neither the first nor the lastIndex of the array.

# Find the index of the peak element. Assume there is only one peak element.

# Input: 0 1 2 3 2 1 0

# Output: 3

# Explanation: The largest element is 3, and its index is 3.


def peak_of_mountain_array(arr: list[int]) -> int:
    n = len(arr)
    l = 0
    r = n - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == n - 1 or arr[mid] > arr[mid + 1]:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans 





# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([0, 1, 2, 3, 2, 1, 0], 3),
        ([1, 3, 2], 1),
        ([1, 5, 4, 3], 1),
        ([1, 2, 3, 4, 2], 3),
    ]
    passed = 0
    for arr, expected in TESTS:
        got = peak_of_mountain_array(arr)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {arr} -> peak index {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")