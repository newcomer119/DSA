def three_sum_unique_triplets(nums: list[int], target: int) -> list[list[int]]:
    # sorting the nums and chekcing for duplicates 
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                res.append([nums[i] , nums[left] , nums[right]])
                # check for duplicates for both side 
                while left < right and nums[left] == nums[left + 1]:
                    left +=1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left +=1
                right -= 1

            elif current_sum < target:
                left += 1

            else:
                right -= 1

    return res




    return res


# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(map(tuple, three_sum_unique_triplets([-1, 0, 1, 2, -1, -4], 0)))
    exp = sorted(map(tuple, [[-1, -1, 2], [-1, 0, 1]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] three_sum target=0 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
