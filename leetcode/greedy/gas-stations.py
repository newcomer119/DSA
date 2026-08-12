# 134. Gas Station
# https://leetcode.com/problems/gas-station/
#
# Circular route: gas[i] fuel at station i, cost[i] to go to next station.
# Return starting index to complete circuit once, or -1.
#
# Example: gas = [1,2,3,4,5], cost = [3,4,5,1,2] -> 3


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    res = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            res = i + 1
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5], [4], 0),
    ]
    passed = 0
    for gas, cost, exp in TESTS:
        got = can_complete_circuit(gas, cost)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] start -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
