# 983. Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/
#
# Buy 1-day, 7-day, or 30-day passes to cover all travel days at minimum cost.
#
# Example: days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15] -> 11


def mincost_tickets(days: list[int], costs: list[int]) -> int:
    last_day = days[-1]
    dp = [0] * (last_day + 1)
    travel_days = set(days)

    for i in range(1, last_day + 1):
        if i not in travel_days:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2],
            )
    return dp[last_day]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ]
    passed = 0
    for days, costs, exp in TESTS:
        got = mincost_tickets(days, costs)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] days={days[:4]}... -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
