# Container With Most Water
# You are given an array height where height[i] is the height of a vertical bar at position i. All bars are spaced one unit apart. Two bars and the x-axis form a container that can hold water. The amount of water is (j - i) × min(height[i], height[j]): the width between the bars multiplied by the shorter bar's height, since water spills over the shorter side.

# Find the pair of bars that holds the most water.

# Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Output: 49

# The best pair is bars at index 1 and index 8, with heights 8 and 7. Width is 8 - 1 = 7, shorter height is 7, so the area is 7 × 7 = 49.


def container_with_most_water(arr: list[int]) -> int:
    l,r = 0, len(arr) - 1
    max_area = 0
    while l < r :
        area = (r - l) * min(arr[l] ,arr[r])
        max_area = max(area, max_area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1 

    return max_area
    # l , r = 0 , len(arr) - 1
    # max_area = 0
    # while l <=r :
    #     area = (r - l) * min(arr[l], arr[r])
    #     max_area = max(area, max_area)
    #     if arr[l] < arr[r]:
    #         l += 1
    #     else:
    #         r-= 1

    # return max_area


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([4, 3, 2, 1, 4], 16)]
    passed = 0
    for arr, exp in TESTS:
        got = container_with_most_water(arr)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")