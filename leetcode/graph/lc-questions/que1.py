# 210. Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        return self.topo_sort(graph, numCourses)

    def find_indegree(self,graph,numCourses):
        indegree = {node : 0 for node in range(numCourses)}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    def topo_sort(self,graph,numCourses):
        res = []
        q = deque()
        indegree = self.find_indegree(graph,numCourses)
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)


        return res if len(res) == len(graph) else []
        # res = []
        # q = deque()
        # indegree = self.find_indegree(graph,numCourses)

        # for node in indegree:
        #     if indegree[node] == 0:
        #         q.append(node)

        # while q:
        #     node = q.popleft()
        #     res.append(node)

        #     for neighbor in graph[node]:
        #         indegree[neighbor] -= 1
        #         if indegree[neighbor] == 0:
        #             q.append(neighbor)


        # return res if len(res) == len(graph) else []

# --- Daily tests ---
if __name__ == "__main__":
    def is_valid_order(order, n, prereqs):
        if not order:
            return n == 0 or bool(prereqs)
        if len(order) != n or len(set(order)) != n:
            return False
        pos = {c: i for i, c in enumerate(order)}
        for course, prereq in prereqs:
            if pos[prereq] >= pos[course]:
                return False
        return True

    sol = Solution()
    TESTS = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], None),
        (1, [], [0]),
    ]
    passed = 0
    for n, prereqs, exp in TESTS:
        got = sol.findOrder(n, prereqs)
        ok = is_valid_order(got, n, prereqs) if exp is None else got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
