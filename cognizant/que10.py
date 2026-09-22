def maximum_jobs(jobs):
    jobs.sort(key=lambda x : x[1])
    last_end = float("-inf")
    count = 0
    for start, end in jobs:
        if start >= last_end:
            count += 1
            last_end = end

    return count



# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        (
            [[1,3], [2,4], [3,5], [4,6], [5,7]],
            3
        ),

        (
            [[1,10], [2,3], [3,4], [4,5]],
            3
        ),

        (
            [[1,2], [2,3], [3,4], [4,5]],
            4
        ),

        # Everything overlaps
        (
            [[1,10], [2,9], [3,8], [4,7]],
            1
        ),

        # Completely separate
        (
            [[1,2], [3,4], [5,6], [7,8]],
            4
        ),

        # Same starting time
        (
            [[1,10], [1,2], [1,5], [2,3]],
            2
        ),

        # Unsorted input
        (
            [[8,9], [1,3], [5,7], [3,5]],
            4
        ),

        # Choosing short jobs is important
        (
            [[1,100], [2,3], [3,4], [4,5],
             [5,6], [6,7]],
            5
        ),

        # Single job
        (
            [[10,20]],
            1
        ),

        # Mixed
        (
            [[1,4], [3,5], [0,6], [5,7],
             [3,9], [5,9], [6,10], [8,11],
             [8,12], [2,14], [12,16]],
            4
        ),
    ]

    passed = 0

    for i, (jobs, expected) in enumerate(tests, 1):

        result = maximum_jobs(jobs)

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