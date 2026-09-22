def maximum_production_profit(profit, k):
    dp = {}
    def dfs(i,rem):
        if i >= len(profit):
            return 0
        if rem == 0:
            return 0

        if (i,rem) in dp:
            return dp[(i,rem)]

        produce = profit[i]  + dfs(i + 2,rem - 1)
        skip = dfs(i + 1 ,rem)

        dp[(i,rem)] = max(skip,produce)
        return dp[(i,rem)]
    return dfs(0,k)


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Basic
        ([5, 1, 10, 5], 2, 15),

        # Only one selection allowed
        ([4, 10, 3, 1, 5], 1, 10),

        # Standard
        ([2, 7, 9, 3, 1], 2, 11),

        # k larger than necessary
        ([2, 7, 9, 3, 1], 10, 12),

        # Single element
        ([20], 1, 20),

        # All equal
        ([5, 5, 5, 5, 5], 2, 10),

        # Best values separated
        ([10, 1, 20, 1, 30], 3, 60),

        # Adjacent large values
        ([1, 100, 100, 1], 2, 101),

        # Zero values
        ([0, 0, 0, 0], 2, 0),

        # k limits otherwise better solution
        ([8, 1, 9, 1, 10, 1, 11], 2, 21),
    ]

    passed = 0

    for i, (profit, k, expected) in enumerate(tests, 1):

        result = maximum_production_profit(profit, k)

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