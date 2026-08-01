# DSA Templates — copy the section you need into a new problem file
# Each block: header comment + skeleton + optional mini test under if __name__


# =============================================================================
# BINARY SEARCH — Find First True
# Use when: sorted/monotonic range splits False...False | True...True
# Examples: first bad version, first element >= target
# =============================================================================

def find_first_true(n: int, is_true) -> int:
    l, r = 0, n
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if is_true(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


# =============================================================================
# BINARY SEARCH — Standard (exact match)
# Use when: find a specific value in a sorted array
# =============================================================================

def binary_search(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# =============================================================================
# TWO POINTERS — Opposite Direction
# Use when: sorted array pair/triplet sum, palindrome, container with water
# =============================================================================

def two_pointer_opposite(arr: list[int], target: int) -> list[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        curr = arr[l] + arr[r]
        if curr == target:
            return [l, r]
        if curr < target:
            l += 1
        else:
            r -= 1
    return []


# =============================================================================
# TWO POINTERS — Same Direction (slow / fast)
# Use when: in-place filtering, remove dups, move zeros
# =============================================================================

def same_direction(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:  # replace with your condition
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# =============================================================================
# TWO POINTERS — Fast / Slow (linked list)
# Use when: cycle detection, find middle, remove nth from end
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# =============================================================================
# SLIDING WINDOW — Fixed Size k
# Use when: max/min/sum of every subarray of length k
# =============================================================================

def fixed_window(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    best = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        best = max(best, window_sum)
    return best


# =============================================================================
# SLIDING WINDOW — Variable Size (longest valid)
# Use when: longest substring/subarray satisfying a condition
# =============================================================================

def variable_longest(s: str) -> int:
    longest = 0
    left = 0
    window = set()  # or dict/counter
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        longest = max(longest, right - left + 1)
    return longest


# =============================================================================
# SLIDING WINDOW — Variable Size (shortest valid)
# Use when: smallest subarray with sum >= target, min window substring
# =============================================================================

def variable_shortest(nums: list[int], target: int) -> int:
    length = len(nums) + 1
    left = 0
    window_sum = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            length = min(length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if length > len(nums) else length


# =============================================================================
# PREFIX SUM + HashMap
# Use when: subarray sum equals k, count subarrays with given sum
# =============================================================================

def prefix_sum_subarray(nums: list[int], target: int) -> list[int]:
    prefix = {0: 0}
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        complement = curr_sum - target
        if complement in prefix:
            return [prefix[complement], i + 1]
        prefix[curr_sum] = i + 1
    return []


# =============================================================================
# GRAPH BFS — Unweighted (level-by-level)
# Use when: shortest path in unweighted graph
# Prereq: graph[i] = list of neighbors
# =============================================================================

from collections import deque


def bfs_unweighted(graph: list[list[int]], start: int, target: int) -> int:
    def get_neighbors(node):
        return graph[node]

    queue = deque([start])
    visited = {start}
    level = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node == target:
                return level
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        level += 1
    return -1


# =============================================================================
# MATRIX BFS — Single Source
# Use when: flood fill, shortest path in grid, knight moves
# =============================================================================

def matrix_bfs(grid: list[list[int]], start: tuple[int, int]) -> set[tuple[int, int]]:
    if not grid or not grid[0]:
        return set()
    rows, cols = len(grid), len(grid[0])

    def get_neighbors(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    queue = deque([start])
    visited = {start}
    while queue:
        r, c = queue.popleft()
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            queue.append((nr, nc))
    return visited


# =============================================================================
# MATRIX DFS — Flood Fill / Count Islands
# Use when: count connected components, explore region
# =============================================================================

def matrix_dfs(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def get_neighbors(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def dfs(r, c):
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        for nr, nc in get_neighbors(r, c):
            dfs(nr, nc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c)
                count += 1
    return count


# =============================================================================
# MULTI-SOURCE BFS
# Use when: walls and gates, rotten oranges, distance from nearest source
# =============================================================================

def multi_source_bfs(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
    return grid


# =============================================================================
# REVERSE / MULTI-START BFS (from borders)
# Use when: pacific-atlantic, cells reachable from multiple targets
# =============================================================================

def reverse_bfs(heights: list[list[int]], starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
    rows, cols = len(heights), len(heights[0])

    def get_neighbors(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    queue = deque(starts)
    visited = set(starts)
    while queue:
        r, c = queue.popleft()
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) in visited:
                continue
            if heights[nr][nc] < heights[r][c]:
                continue
            visited.add((nr, nc))
            queue.append((nr, nc))
    return visited


# =============================================================================
# TOPOLOGICAL SORT (Kahn's BFS)
# Use when: course schedule, alien dictionary
# =============================================================================

def topo_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    graph = {node: set() for node in range(n)}
    indegree = {node: 0 for node in range(n)}
    for u, v in edges:
        if v not in graph[u]:
            graph[u].add(v)
            indegree[v] += 1
    queue = deque(node for node in indegree if indegree[node] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == n else []


# =============================================================================
# TOPOLOGICAL SORT — Unique Order Check
# Use when: sequence reconstruction (only one valid order allowed)
# =============================================================================

def unique_topo_order(n: int, seqs: list[list[int]], expected: list[int]) -> bool:
    graph = {node: set() for node in range(1, n + 1)}
    indegree = {node: 0 for node in range(1, n + 1)}
    for seq in seqs:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            if v not in graph[u]:
                graph[u].add(v)
                indegree[v] += 1
    queue = deque(node for node in indegree if indegree[node] == 0)
    order = []
    while queue:
        if len(queue) > 1:
            return False
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order == expected


# =============================================================================
# DIJKSTRA — Weighted Shortest Path
# Use when: shortest path with non-negative weights
# =============================================================================

from heapq import heappop, heappush
from math import inf


def dijkstra(graph: list[list[tuple[int, int]]], start: int, target: int) -> int:
    def get_neighbors(node):
        return graph[node]

    queue = [(0, start)]
    distance = [inf] * len(graph)
    distance[start] = 0
    while queue:
        dist, node = heappop(queue)
        if dist > distance[node]:
            continue
        for neighbor, weight in get_neighbors(node):
            d = distance[node] + weight
            if distance[neighbor] <= d:
                continue
            distance[neighbor] = d
            heappush(queue, (d, neighbor))
    res = distance[target]
    return -1 if res == inf else res


# =============================================================================
# TREE BFS — Level Order
# Use when: level-order, zigzag, right-side view, min depth
# =============================================================================

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Node) -> list[list[int]]:
    res = []
    if root is None:
        return res
    queue = deque([root])
    while queue:
        n = len(queue)
        level = []
        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)
            for child in (node.left, node.right):
                if child is not None:
                    queue.append(child)
        res.append(level)
    return res


# =============================================================================
# TREE DFS — Recursive
# Use when: max depth, invert tree, path sum, subtree checks
# =============================================================================

def tree_dfs(root: Node) -> int:
    def dfs(node):
        if node is None:
            return 0
        return max(dfs(node.left), dfs(node.right)) + 1
    return dfs(root) - 1 if root else 0


# =============================================================================
# BACKTRACKING — Choose / Unchoose
# Use when: subsets, combinations, permutations, partition
# =============================================================================

def backtrack_subsets(nums: list[int]) -> list[list[int]]:
    res = []

    def dfs(start_index, path):
        if start_index == len(nums):
            res.append(path[:])
            return
        path.append(nums[start_index])
        dfs(start_index + 1, path)
        path.pop()
        dfs(start_index + 1, path)

    dfs(0, [])
    return res


# =============================================================================
# BACKTRACKING + Memoization
# Use when: word break, coin change count, decode ways
# =============================================================================

def memo_backtrack(s: str, word_set: set[str]) -> bool:
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            w = s[start:end]
            if w in word_set and dfs(end):
                memo[start] = True
                return True
        memo[start] = False
        return False

    return dfs(0)


# =============================================================================
# MIN-HEAP TOP K
# Use when: kth largest, k closest points, k frequent elements
# =============================================================================

def top_k_largest(nums: list[int], k: int) -> int:
    heap = []
    for i in range(k):
        heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heappop(heap)
            heappush(heap, nums[i])
    return heap[0]


# --- Quick sanity check ---
if __name__ == "__main__":
    assert find_first_true(5, lambda v: v >= 4) == 4
    assert binary_search([1, 3, 5, 7], 5) == 2
    assert two_pointer_opposite([2, 3, 4, 5, 8], 8) == [1, 3]
    assert fixed_window([1, 2, 3, 7, 4, 1], 3) == 14
    assert variable_longest("abcabcbb") == 3
    assert variable_shortest([1, 4, 1, 7, 3, 0, 2, 5], 10) == 2
    assert prefix_sum_subarray([1, 2, 3], 5) == [1, 3]
    assert bfs_unweighted([[1, 2], [0, 2, 3], [0, 1], [1]], 0, 3) == 2
    assert topo_sort(3, [(0, 1), (0, 2)]) == [0, 1, 2]
    assert unique_topo_order(3, [[1, 2], [1, 3], [2, 3]], [1, 2, 3]) is True
    assert dijkstra([[(1, 1), (2, 4)], [(2, 2)], [(3, 1)], []], 0, 3) == 4
    assert top_k_largest([3, 2, 1, 5, 6, 4], 2) == 5
    print("All template sanity checks passed.")
