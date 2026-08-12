# 502. IPO
# https://leetcode.com/problems/ipo/
#
# Pick at most k projects to maximize capital. Project i needs capital[i] and gives profits[i].
#
# Example: k=2, w=0, profits=[1,2,3], capital=[0,1,1] -> 4


import heapq


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    min_capital = list(zip(capital, profits))
    heapq.heapify(min_capital)
    max_profit = []

    for _ in range(k):
        while min_capital and min_capital[0][0] <= w:
            _, prof = heapq.heappop(min_capital)
            heapq.heappush(max_profit, -prof)
        if not max_profit:
            break
        w -= heapq.heappop(max_profit)

    return w


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (2, 0, [1, 2, 3], [0, 1, 1], 4),
        (3, 0, [1, 2, 3], [0, 1, 2], 6),
        (1, 0, [1, 2, 3], [0, 1, 2], 1),
    ]
    passed = 0
    for k, w, profits, cap, exp in TESTS:
        got = find_maximized_capital(k, w, profits, cap)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
