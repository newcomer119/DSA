# 322. Coin Change
# https://leetcode.com/problems/coin-change/
#
# Return the fewest coins needed to make amount, or -1 if impossible.
#
# Example: coins = [1, 2, 5], amount = 11 -> 3


def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
    passed = 0
    for coins, amount, exp in TESTS:
        got = coin_change(coins, amount)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] amount={amount} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
