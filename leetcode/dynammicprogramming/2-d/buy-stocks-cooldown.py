# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#
# Unlimited transactions, but must wait 1 day after selling before buying again.
#
# Example: prices = [1, 2, 3, 0, 2] -> 3


def max_profit_cooldown(prices: list[int]) -> int:
    dp = {}

    def dfs(i: int, buying: bool) -> int:
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]
        if buying:
            dp[(i, buying)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
        else:
            dp[(i, buying)] = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
        return dp[(i, buying)]

    return dfs(0, True)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3, 0, 2], 3),
        ([1], 0),
        ([1, 2, 4], 3),
    ]
    passed = 0
    for prices, exp in TESTS:
        got = max_profit_cooldown(prices)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {prices} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
