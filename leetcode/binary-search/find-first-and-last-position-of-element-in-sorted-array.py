def searchRange(nums, target):
    first,last = -1,-1
    l, r = 0,len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            first = mid
            r = mid - 1
        elif nums[mid] > target:
            r = mid -1
        else:
            l = mid + 1

    l,r = 0,len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            last = mid
            l = mid + 1
        elif nums[mid] > target:
            r=  mid - 1
        else:
            l = mid + 1

    return (first,last)
    
    # first,last = -1,-1
    # left,right = 0, len(nums)- 1
    # while left <= right:
    #     mid = (left + right) // 2
    #     if nums[mid] == target:
    #         first = mid
    #         right = mid - 1
    #     elif nums[mid] > target:
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    # left , right = 0, len(nums) - 1
    # while left <= right:
    #     mid = (left +  right) // 2
    #     if nums[mid] == target:
    #         last = mid
    #         left = mid + 1
    #     elif nums[mid] > target:
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    # return (first, last)

    
            
    
    

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([2, 2, 2, 2], 2, [0, 3]),
        ([1], 1, [0, 0]),
        ([1], 2, [-1, -1]),
    ]
    passed = 0
    for nums, target, expected in TESTS:
        got = list(searchRange(nums, target))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")
