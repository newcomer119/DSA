# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/
#
# Return the number of combinations to make amount.
#
# Example: amount = 5, coins = [1, 2, 5] -> 4


def coin_change_ii(amount: int, coins: list[int]) -> int:
    dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
    ]
    passed = 0
    for amount, coins, exp in TESTS:
        got = coin_change_ii(amount, coins)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] amount={amount} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
