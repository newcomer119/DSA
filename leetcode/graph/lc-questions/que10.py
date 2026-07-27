# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

import heapq
from math import inf
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((time, dst))

        queue = [(0, k)]
        delay_time = [inf] * (n + 1)
        delay_time[k] = 0

        while queue:
            cur_time, cur_node = heapq.heappop(queue)
            if cur_time > delay_time[cur_node]:
                continue

            for edge in graph[cur_node]:
                new_time,new_node = edge 
                if delay_time[new_node] > cur_time + new_time:
                    delay_time[new_node] = cur_time + new_time
                    heapq.heappush(queue, (delay_time[new_node], new_node))


        max_delay = max(delay_time[1:])
        return max_delay if max_delay != inf else -1


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ]
    passed = 0
    for times, n, k, exp in TESTS:
        got = sol.networkDelayTime(times, n, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
