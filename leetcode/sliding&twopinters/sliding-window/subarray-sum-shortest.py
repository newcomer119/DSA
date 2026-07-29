# Flexible Size Sliding Window
# Let's continue on finding the sum of subarrays. This time given a positive integer array nums, we want to find the length of the shortest subarray such that the subarray sum is at least target. Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10, then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.

# We'll assume for this problem that it's guaranteed target will not exceed the sum of all


def subarray_sum_shortest(nums: list[int], target: int) -> int:
   # shortest subarray whoose sum will be equivalent to target 
    length = len(nums) + 1
    left = 0
    wsum = 0
    for right in range(len(nums)):
        wsum += nums[right]
        while wsum >= target:
            length = min(length, right - left  + 1)
            wsum -= nums[left]
            left += 1

    if length > len(nums):return 0

    return length

    
    # window_sum = 0
    # length = len(nums) + 1 # So len(nums) + 1 is impossible as a real answer, which makes it a safe “placeholder”
    # left = 0
    # for right in range(len(nums)):
    #     window_sum += nums[right] 
    #     while window_sum >= target:
    #         length = min(length, right - left + 1)
    #         window_sum -= nums[left] 
    #         left += 1
    # if length > len(nums):
    #     return 0
    # return length


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 4, 1, 7, 3, 0, 2, 5], 10, 2), ([2, 3, 1, 2, 4, 3], 7, 2), ([1, 1, 1, 1], 10, 0)]
    passed = 0
    for nums, target, exp in TESTS:
        got = subarray_sum_shortest(nums, target)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")