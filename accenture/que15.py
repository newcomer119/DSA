def strong_growth_sum(sales: list[int], k: int) -> int:
    """
    Return the sum of sales values on strong growth days.

    A strong growth day:
    - is not the first day
    - sales[i] > sales[i - 1]
    - sales[i] - sales[i - 1] >= k
    """

    # Write your solution here

    total = 0
    values = []
    for i in range(1, len(sales)):
        if (sales[i] > sales[i- 1] and abs(sales[i] - sales[i-1]) >= k):
            values.append(sales[i])


    for value in values:
        total +=value
    return total


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ([10, 15, 18, 30, 32], 5, 45),
    ([5, 10, 15], 5, 25),
    ([10, 12, 14, 16], 5, 0),
    ([20, 10, 30, 25, 40], 10, 70),
    ([1, 2, 10, 11, 20], 8, 30),
    ([100], 10, 0),
    ([10, 10, 20], 10, 20),
]


# ==========================================
# TEST RUNNER
# ==========================================

for sales, k, expected in test_cases:
    result = strong_growth_sum(sales, k)

    print(f"sales    = {sales}")
    print(f"k        = {k}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)