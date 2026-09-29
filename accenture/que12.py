def count_peak_sales_days(sales: list[int]) -> int:
    """
    Return the number of peak sales days.

    A peak is strictly greater than BOTH
    its previous and next day's sales.

    First and last elements cannot be peaks.
    """

    # Write your solution here
    count= 0
    for i in range(1, len(sales) - 1):
        if sales[i] > sales[i-1] and sales[i] > sales[i + 1]:
            count += 1

    return count



# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([10, 25, 15, 30, 20], 2),

    ([1, 3, 2], 1),

    ([1, 2, 3, 4, 5], 0),

    ([5, 4, 3, 2, 1], 0),

    ([10, 20, 20, 10], 0),

    ([5, 10, 5, 10, 5, 10, 5], 3),

    ([7], 0),

    ([4, 9], 0),

    ([3, 8, 4, 6, 2, 7, 1], 3),
]


# ==========================================
# TEST RUNNER
# ==========================================

for sales, expected in test_cases:
    result = count_peak_sales_days(sales)

    print(f"sales    = {sales}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)