def count_high_growth_days(sales: list[int], k: int) -> int:
    # your solution
    # A company stores daily sales in an integer array sales.
    # A day is considered a high growth day if:
    # - it is not the first day,
    # - today's sales are strictly greater than yesterday's sales,
    # - and the increase from yesterday is at least k.
    count = 0

    for i in range(1, len(sales)):
        if sales[i] > sales[i - 1] and sales[i] - sales[i - 1] >= k:
            count += 1

    return count


test_cases = [
    ([100, 120, 125, 160, 170], 20, 2),
    ([10, 20, 30, 40], 10, 3),
    ([10, 15, 18, 20], 10, 0),
    ([50, 30, 70, 60, 100], 30, 2),
    ([100], 20, 0),
    ([10, 10, 20], 10, 1),
]

for sales, k, expected in test_cases:
    result = count_high_growth_days(sales, k)

    print("sales:", sales)
    print("k:", k)
    print("expected:", expected)
    print("got:", result)
    print("PASS" if result == expected else "FAIL")
    print("-" * 30)
