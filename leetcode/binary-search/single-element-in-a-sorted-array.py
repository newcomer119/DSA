# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105


def singleNonDuplicate(nums):
    def to_the_left(idx):
        if (idx == len(nums)-1):
            return True
        elif (idx % 2):   # odd
            return nums[idx] != nums[idx-1]
        else:             # even
            return nums[idx] != nums[idx+1]

    left, right, ans = 0, len(nums)-1, -1
    while left <= right:
        mid = (left + right) // 2
        if to_the_left(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return nums[ans]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([9], 9),
        ([1, 1, 2, 2, 3], 3),
        ([1, 2, 2, 3, 3], 1),
    ]
    passed = 0
    for nums, expected in TESTS:
        got = singleNonDuplicate(nums)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")