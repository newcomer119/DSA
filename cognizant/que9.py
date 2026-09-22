def minimum_processing_days(target, shipments):
    left = 0
    shortest = len(shipments) + 1
    wsum = 0

    for right in range(len(shipments)):
        wsum += shipments[right]
        while wsum >= target:
            shortest = min(shortest, right - left + 1)
            wsum -= shipments[left]
            left += 1
    return shortest if shortest != len(shipments) + 1 else 0


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Standard
        (7, [2, 3, 1, 2, 4, 3], 2),

        # Single element works
        (4, [1, 4, 4], 1),

        # Impossible
        (20, [2, 3, 4], 0),

        # Entire array needed
        (15, [1, 2, 3, 4, 5], 5),

        # Exact target
        (6, [1, 2, 3], 3),

        # Shrink several times
        (11, [1, 2, 3, 4, 5], 3),

        # Large first element
        (8, [10, 1, 1, 1], 1),

        # Repeated values
        (8, [2, 2, 2, 2, 2], 4),

        # Best window near end
        (10, [1, 1, 1, 1, 6, 4], 2),

        # Single element impossible
        (10, [5], 0),
    ]

    passed = 0

    for i, (target, shipments, expected) in enumerate(tests, 1):

        result = minimum_processing_days(target, shipments)

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
