# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# Pay cost[i] to step on i, then climb 1 or 2 steps. Start at index 0 or 1.
#
# Example: cost = [10, 15, 20] -> 15


def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    if n <= 1:
        return 0
    prev2, prev1 = cost[0], cost[1]
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    return min(prev1, prev2)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0, 1], 0),
    ]
    passed = 0
    for cost, exp in TESTS:
        got = min_cost_climbing_stairs(cost)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {cost[:4]}... -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
