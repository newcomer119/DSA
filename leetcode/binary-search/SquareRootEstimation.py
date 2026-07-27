# Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

# Input: 16

# Output: 4

# Input: 8

# Output: 2

# Explanation: square root of 8 is 2.83..., return the integer part, 2



def square_root(n: int) -> int:
    # left , right = 0, n
    # ans = -1
    # while left <= right:
    #     mid = (left + right) // 2
    #     if mid * mid == n:
    #         return mid
    #     elif mid * mid  > n:
    #         ans = mid
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return ans - 1


    l, r = 0,  n
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans - 1

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(16, 4), (8, 2), (0, 0), (1, 1), (26, 5)]
    passed = 0
    for n, expected in TESTS:
        got = square_root(n)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] sqrt({n}) -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")