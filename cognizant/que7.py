def maximum_capacity_limit(capacity, limit):
    # we need to find highest valid number 
    def feasible(x):
        total = 0
        for cap in capacity:
            total +=  min(cap,x)

            if total > limit:
                return False 
        return True 

        


    l,r = 0, max(capacity)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if feasible(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans 
        
        



# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Basic
        ([3, 8, 10, 12], 27, 8),

        # Everything gets reduced
        ([5, 5, 5], 9, 3),

        # No reduction required
        ([2, 4, 6], 100, 6),

        # Single server
        ([100], 50, 50),

        # Exact existing total
        ([2, 3, 5], 10, 5),

        # Uneven capacities
        ([4, 7, 9, 15], 25, 7),

        # Large values
        ([1000000000, 1000000000], 1000000000, 500000000),

        # Very small limit
        ([10, 20, 30], 3, 1),

        # Mixed
        ([1, 10, 20, 30], 31, 10),

        # Another boundary case
        ([6, 6, 6, 6], 20, 5),
    ]

    passed = 0

    for i, (capacity, limit, expected) in enumerate(tests, 1):

        result = maximum_capacity_limit(capacity, limit)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED | "
                f"expected={expected}, got={result}"
            )

    print(f"\nRESULT: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()