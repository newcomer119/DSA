# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. Do this in-place using constant auxiliary space.

# Input:

# [1, 0, 2, 0, 0, 7]
# Output:

# [1, 2, 7, 0, 0, 0]


def move_zeros(nums: list[int]) -> None:
    # slow = 0
    # for fast in range(len(nums)):
    #     if nums[fast] != 0:
    #         nums[slow], nums[fast] = nums[fast], nums[slow]
    #         slow += 1


    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow],nums[fast] = nums[fast], nums[slow]
            slow += 1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 0, 2, 0, 0, 7], [1, 2, 7, 0, 0, 0]), ([0, 0, 1], [1, 0, 0]), ([1, 2, 3], [1, 2, 3])]
    passed = 0
    for nums, exp in TESTS:
        data = nums[:]
        move_zeros(data)
        ok = data == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {data}")
    print(f"\n{passed}/{len(TESTS)} passed")