def count_stable_days(sales: list[int], k: int) -> int:
    """
    A stable day must:

    1. Not be the first or last day.
    2. Have sales greater than the previous day.
    3. Have an absolute difference with the next day <= k.

    Return the number of stable days.
    """

    # Write your solution here
    count = 0
    for i in range(1, len(sales)- 1):
        if (sales[i] < sales[i-1] and abs(sales[i] - sales[i + 1]) <= k):
            count += 1
    return count


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([10, 20, 18, 30, 27], 3, 2),

    ([5, 10, 8], 2, 1),

    ([1, 2, 10, 11], 3, 0),

    ([10, 5, 4, 3], 10, 0),

    ([2, 6, 4, 8, 7, 10, 8], 2, 3),

    ([5], 10, 0),

    ([5, 10], 10, 0),
]


# ==========================================
# TEST RUNNER
# ==========================================

for sales, k, expected in test_cases:
    result = count_stable_days(sales, k)

    print(f"sales    = {sales}")
    print(f"k        = {k}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)