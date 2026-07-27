# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

def firstBadVersion(n: int) -> int:
        # l,r = 0 ,n
        # ans = -1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if isBadVersion(mid):
        #         ans = mid
        #         r = mid-1
        #     else:
        #         l = mid + 1

        # return ans

        l,r = 0, n
        ans = -1
        while l <=r :
            mid = (l + r) // 2
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else : 
                l = mid + 1
        return ans 

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(5, 4), (1, 1), (10, 1), (10, 10)]
    passed = 0
    for n, expected in TESTS:
        bad = expected

        def isBadVersion(version, bad=bad):
            return version >= bad

        l, r, ans = 0, n, -1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        got = ans
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n}, first bad={expected} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")