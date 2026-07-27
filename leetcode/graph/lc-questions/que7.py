# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]


from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # 1. Build the Graph (Adjacency List)
        # Each node points to neighbors with the corresponding ratio
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))      # a / b = val
            graph[b].append((a, 1.0 / val)) # b / a = 1 / val

        # 2. BFS Function
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            # Queue stores: (current_node, current_product_value)
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                curr_node, curr_val = queue.popleft()
                
                # Check neighbors
                for neighbor, weight in graph[curr_node]:
                    if neighbor == end:
                        return curr_val * weight
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_val * weight))
            
            return -1.0

        # 3. Main Logic
        results = []
        for start, end in queries:
            results.append(bfs(start, end))
            
        return results


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.0, 0.5, -1.0, 1.0, -1.0],
        ),
        (
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"]],
            [0.5, 2.0],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75, 0.4, 5.0, 0.2],
        ),
    ]
    passed = 0
    for eqs, vals, queries, exp in TESTS:
        got = sol.calcEquation(eqs, vals, queries)
        ok = all(abs(g - e) < 1e-5 for g, e in zip(got, exp))
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(queries)} queries -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
