# Input: arr = [false, false, true, true, true]

# Output: 2


def find_boundary(arr: list[bool]) -> int:
    left, right = 0 ,len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid- 1
        else:
            left = mid + 1
    return boundary_index


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([False, False, True, True, True], 2),
        ([True, True, True], 0),
        ([False, False, True], 2),
        ([False], -1),
        ([True], 0),
    ]
    passed = 0
    for arr, expected in TESTS:
        got = find_boundary(arr)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {arr} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")