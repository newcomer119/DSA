def maximum_maintenance(maintenance):
    n = len(maintenance)

    if n == 1:
        return maintenance[0]

    dp = [0] * n                                                                                                                        

    dp[0] = maintenance[0]
    dp[1] = max(maintenance[0], maintenance[1])

    for i in range(2, n):
        dp[i] = max(
            maintenance[i] + dp[i - 2],  # TAKE
            dp[i - 1]                    # SKIP
        )

    return dp[n - 1]

# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Basic
        ([2, 7, 9, 3, 1], 12),

        # Mixed
        ([5, 1, 2, 10, 6, 2], 17),

        # Two elements
        ([10, 20], 20),

        # Single element
        ([50], 50),

        # All equal
        ([5, 5, 5, 5], 10),

        # Large middle value
        ([1, 2, 100, 2, 1], 102),

        # Alternating
        ([10, 1, 10, 1, 10], 30),

        # Zeros
        ([0, 0, 0, 0], 0),

        # Greedy-looking trap
        ([6, 10, 12, 7, 9, 14], 36),

        # Another case
        ([4, 1, 1, 9, 1, 1, 4], 17),
    ]

    passed = 0

    for i, (maintenance, expected) in enumerate(tests, 1):

        result = maximum_maintenance(maintenance)

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