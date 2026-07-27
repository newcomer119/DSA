# Prereq: Topological Sort

# For this problem, given a list of tasks and a list of requirements, compute a sequence of tasks that can be performed, such that we complete every task once while satisfying all the requirements.

# Each requirement will be in the form of a list [a, b], where task a needs to be completed first before task b can be completed,

# There is guaranteed to be a solution.

# Examples
# Example 1
# Input:
# tasks = ["a", "b", "c", "d"]
# requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
# Output: ["a", "c", "b", "d"]


from collections import deque

def find_indegree(graph):
    indegree = {node : 0 for node in graph}
    for node in graph:
        for neighbors in graph[node]:
            indegree[neighbors] += 1
    return indegree
def topo_sort(graph):
    res =[]
    q = deque()
    indegree = find_indegree(graph)
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
    return res if len(graph) == len(res) else None
def task_scheduling(tasks: list[str], requirements: list[list[str]]) -> list[str]:
    graph = {t : [] for t in tasks}
    for a,b in requirements:
        graph[a].append(b)
    return topo_sort(graph) or []


# --- Daily tests ---
if __name__ == "__main__":
    def is_valid_task_order(order, tasks, requirements):
        if len(order) != len(tasks):
            return False
        pos = {t: i for i, t in enumerate(order)}
        for a, b in requirements:
            if pos[a] >= pos[b]:
                return False
        return True

    TESTS = [
        (["a", "b", "c", "d"], [["a", "b"], ["c", "b"], ["b", "d"]]),
        (["a", "b"], [["a", "b"]]),
        (["x", "y", "z"], [["x", "y"], ["y", "z"]]),
    ]
    passed = 0
    for tasks, requirements in TESTS:
        got = task_scheduling(tasks, requirements)
        ok = is_valid_task_order(got, tasks, requirements)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {tasks} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

