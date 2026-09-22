from heapq import heappop, heappush

def minimum_vehicles(bookings):
    bookings.sort(key = lambda x : x[0])
    heap = []
    vechiles = 0
    for start, end in bookings:
        if heap and heap[0] <= start:
            heappop(heap)
        heappush(heap, end)
        vechiles = max(vechiles, len(heap))

    return vechiles


# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        (
            [[1, 4], [2, 5], [7, 9]],
            2
        ),

        (
            [[1, 3], [3, 6], [6, 8]],
            1
        ),

        (
            [[1, 10], [2, 7], [3, 5], [6, 8]],
            3
        ),

        # Every booking overlaps
        (
            [[1, 10], [2, 9], [3, 8], [4, 7]],
            4
        ),

        # Completely separate
        (
            [[1, 2], [3, 4], [5, 6], [7, 8]],
            1
        ),

        # Same start time
        (
            [[1, 5], [1, 3], [1, 7]],
            3
        ),

        # Vehicle becomes available exactly in time
        (
            [[1, 5], [5, 10], [10, 15]],
            1
        ),

        # Mixed
        (
            [[1, 4], [2, 3], [3, 6], [5, 7], [8, 10]],
            2
        ),

        # Single booking
        (
            [[100, 200]],
            1
        ),
    ]

    passed = 0

    for i, (bookings, expected) in enumerate(tests, 1):

        result = minimum_vehicles(bookings)

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