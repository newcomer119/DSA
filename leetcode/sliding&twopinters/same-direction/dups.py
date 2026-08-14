# Given a sorted list of numbers with length at least 1, remove duplicates and return the new length. You must do this in-place and without using extra memory.

# Input: [0, 0, 1, 1, 1, 2, 2].

# Output: 3.

# Your function should modify the list in place so that the first three elements become 0, 1, 2. Return 3 because the new length is 3.



def remove_duplicates(arr: list[int]) -> int:
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1

        arr[slow] = arr[fast]
    return slow + 1
# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([0, 0, 1, 1, 1, 2, 2], 3, [0, 1, 2]), ([1, 1, 1], 1, [1]), ([1, 2, 3], 3, [1, 2, 3])]
    passed = 0
    for arr, exp_len, exp_prefix in TESTS:
        data = arr[:]
        got_len = remove_duplicates(data)
        ok = got_len == exp_len and data[:exp_len] == exp_prefix
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] len={got_len}, prefix={data[:got_len]}")
    print(f"\n{passed}/{len(TESTS)} passed")