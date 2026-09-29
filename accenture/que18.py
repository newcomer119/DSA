def count_sudden_drops(prices: list[int], k: int) -> int:
#     A day is a sudden drop day if:
# - it is not the first day;
# - today's price is strictly lower than yesterday's price;
# - the decrease is at least k.
# - Return the number of sudden drop days.
    count = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1] and prices[i] - prices[i-1] <= k:
            count+= 1

    return count 

test_cases = [
    ([100, 70, 65, 40, 50], 20, 2),
    ([50, 40, 30, 20], 10, 3),
    ([10, 20, 30], 5, 0),
    ([100, 90, 50, 45, 10], 30, 2),
    ([100], 10, 0),
    ([20, 20, 10], 10, 1),
]


for prices, k, expected in test_cases:
    result = count_sudden_drops(prices, k)

    print("prices:", prices)
    print("k:", k)
    print("expected:", expected)
    print("got:", result)
    print("PASS" if result == expected else "FAIL")
    print("-" * 30)