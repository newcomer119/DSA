# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# Constraints:
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

from math import ceil,inf
from typing import List

def can_finish(piles,h,k):
    hours = 0
    for p in piles:
        hours += ceil(float(p)/k)
    return hours <= h


def minEatingSpeed(piles , h):
    l, r = 1 , 1000000000
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if can_finish(piles,h,mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans 

# def can_finish(piles, h, k):
#     hours = 0
#     for p in piles:
#         hours += ceil(float(p)/k)
#     return hours <= h
   
# def minEatingSpeed(piles: List[int], h: int) -> int:
#     left, right = 1, 1000000000
#     ans = -1
#     while left<=right:
#         mid = (left + right) // 2
#         if can_finish(piles, h, mid):
#             ans = mid
#             right = mid - 1

#         else:
#             left = mid + 1
#     return ans



# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([10], 5, 2),
        ([3, 6, 7, 11], 11, 3),
    ]
    passed = 0
    for piles, h, expected in TESTS:
        got = minEatingSpeed(piles, h)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] piles={piles}, h={h} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")