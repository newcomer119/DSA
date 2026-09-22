def count_target_transactions(transactions, target):
    prefix_count = {0: 1}
    curr_sum = 0
    count = 0
    for num in transactions:
        curr_sum += num
        csum = curr_sum - target
        if csum in prefix_count:
            count += prefix_count[csum]
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
    return count



# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Basic
        ([1, 1, 1], 2, 2),

        # Whole range + individual element
        ([1, 2, 3], 3, 2),

        # Negative numbers and zero
        ([1, -1, 0], 0, 3),

        # Single element
        ([5], 5, 1),

        # No valid sequence
        ([1, 2, 3], 100, 0),

        # Multiple zeros
        ([0, 0, 0], 0, 6),

        # Negative values
        ([3, 4, -7, 1, 3, 3, 1, -4], 7, 4),

        # Negative target
        ([-1, -1, 1], -1, 3),

        # Repeated prefix sums
        ([1, -1, 1, -1, 1], 0, 6),

        # Larger case
        ([2, 3, -2, 5, -3, 1, 2], 5, 5),
    ]

    passed = 0

    for i, (transactions, target, expected) in enumerate(tests, 1):

        result = count_target_transactions(transactions, target)

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