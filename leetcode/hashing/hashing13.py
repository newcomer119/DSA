# Minimum Steps to Make All Piles Equal
# GFG: https://www.geeksforgeeks.org/minimum-number-of-steps-to-make-all-elements-of-array-equal/
# LeetCode (related): https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
#
# In one step, pick the largest pile and reduce it to the second-largest height.
# Return the minimum number of steps until all piles are equal.
#
# Example:
# piles = [5, 2, 1] -> 4


from collections import Counter


def minimum_steps(piles: list[int]) -> int:
    piles = piles[:]
    steps = 0
    while True:
        unique = sorted(set(piles), reverse=True)
        if len(unique) <= 1:
            break
        large1, large2 = unique[0], unique[1]
        for i in range(len(piles)):
            if piles[i] == large1:
                piles[i] = large2
                steps += 1
                break
    return steps


def minimum_steps_optimized(piles: list[int]) -> int:
    freq = Counter(piles)
    sorted_unique_heights = sorted(freq.keys(), reverse=True)
    steps = 0
    accumulated_piles = 0
    for i in range(len(sorted_unique_heights) - 1):
        accumulated_piles += freq[sorted_unique_heights[i]]
        steps += accumulated_piles
    return steps


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([5, 2, 1], 3),
        ([1, 1, 1], 0),
        ([4, 3, 2, 1], 6),
    ]
    passed = 0
    for piles, exp in TESTS:
        got = minimum_steps_optimized(piles)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {piles} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
