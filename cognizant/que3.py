def longest_access_period(accessLogs, k):
    freq = {}
    left = 0
    max_length = 0

    for right in range(len(accessLogs)):
        freq[accessLogs[right]] = freq.get(accessLogs[right], 0) + 1
        while len(freq) > k:
            freq[accessLogs[left]] -= 1
            if freq[accessLogs[left]] == 0:
                del freq[accessLogs[left]]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length
# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Basic
        ([1, 2, 1, 2, 3], 2, 4),

        # Multiple possible windows
        ([1, 2, 1, 3, 4, 2, 3], 2, 3),

        # One employee
        ([5, 5, 5, 5], 1, 4),

        # k allows everything
        ([1, 2, 3, 4, 5], 5, 5),

        # Only one distinct allowed
        ([1, 2, 2, 2, 3], 1, 3),

        # Entire array has two employees
        ([1, 2, 1, 2, 1, 2], 2, 6),

        # Window needs to shrink multiple times
        ([1, 2, 3, 2, 2, 3, 4], 2, 5),

        # Single element
        ([100], 1, 1),

        # Larger mixed case
        ([1, 2, 1, 3, 3, 3, 2, 2, 4, 4], 2, 5),
    ]

    passed = 0

    for i, (logs, k, expected) in enumerate(tests, 1):

        result = longest_access_period(logs, k)

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