from math import inf

def min_coins(coins, amount, sum, memo):
  if sum == amount:
    return 0

  if sum > amount:
    return inf

  if (memo[sum] != -1):
    return memo[sum]

  ans = inf
  for coin in coins:
    result = min_coins(coins, amount, sum + coin, memo)
    if result == inf:
      continue
    ans = min(ans, result + 1)

  memo[sum] = ans
  return ans

def coin_change(coins: list[int], amount: int) -> int:
  memo = [-1] * (amount + 1)
  result = min_coins(coins, amount, 0, memo)
  return result if result != inf else -1

  return result if result != inf else -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0)]
    passed = 0
    for coins, amount, exp in TESTS:
        got = coin_change(coins, amount)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] amount={amount} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
