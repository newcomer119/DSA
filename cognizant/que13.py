def longest_safe_period(traffic, limit):
    # traffic arr limit = k
    wsum = 0
    left = 0
    longest = 0

    for right in range(len(traffic)):
        wsum += traffic[right]
        while wsum > limit:
            wsum -= traffic[left]
            left += 1
        longest = max(longest, right - left + 1)

    return longest if longest != 0 else 0


def run_tests():

    tests = [
        ([2, 1, 3, 2, 1, 1, 5], 7, 4),

        ([1, 1, 1, 1, 1], 3, 3),

        ([10, 1, 1, 1], 5, 3),

        ([1, 2, 3], 100, 3),

        ([5], 4, 0),

        ([5], 5, 1),

        ([2, 2, 2, 2], 4, 2),

        ([1, 4, 2, 1, 1, 1], 5, 4),

        ([3, 1, 2, 1, 1, 1, 5], 6, 5),
    ]

    passed = 0

    for i, (traffic, limit, expected) in enumerate(tests, 1):

        result = longest_safe_period(
            traffic,
            limit
        )

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED | "
                f"expected={expected}, got={result}"
            )

    print(
        f"\nRESULT: "
        f"{passed}/{len(tests)} tests passed"
    )


if __name__ == "__main__":
    run_tests()