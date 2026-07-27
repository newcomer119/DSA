# Note that this problem requires knowing heap, which is covered in the Priority Queue/Heap section. If you are working through the content in order, feel free to skip this problem and come back after you have completed the heap section.

# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.

# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.

# Derive the order of letters in this language.

# Note:

# You may assume all letters are in lowercase.
# Every letter that appears in the input must also appear in the output, and your output cannot have characters not in the input.
# If no ordering of letters makes the dictionary sorted lexicographically, return an empty string.
# There may be multiple valid orders. If that's the case, return the smallest in normal lexicographical order.
# Input & Output
# Input
# words — A list of strings of size `n`, representing the dictionary words sorted lexicographically in the alien language.
# Output
# A string representing the smallest possible lexicographical order, or an empty string if no valid order exists.
# Example
# Input
# words = ["wrt","wrf","er","ett","rftt"]
# Output
# wertf
# Explanation


# Example
# Input
# words = ["z","x"]
# Output
# zx
# Explanation
# From z and x，we can get z < x. So return zx.

# Constraints
# 2 <= n <= 10000
# 1 <= words[i].length <= 30



from heapq import heappop, heappush

def find_indegree(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree


def topo_sort(graph):
    res = []
    pq = []
    indegree = find_indegree(graph)

    for node in indegree:
        if indegree[node] == 0:
            heappush(pq, node)

    while len(pq) > 0:
        node = heappop(pq)
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heappush(pq, neighbor)

    for indeg in indegree.values():
        if indeg != 0:
            return None
    return res
        
def alien_order(words):
    graph = {}
    for word in words:
        for c in word:
            if c not in graph:
                graph[c] = []

    prev = words[0]
    for i in range(1, len(words)):
        cur = words[i]
        j = 0
        while j < len(prev) and j < len(cur):
            if prev[j] != cur[j]:
                if cur[j] not in graph[prev[j]]:
                    graph[prev[j]].append(cur[j])
                break
            j += 1

        if prev.startswith(cur) and len(prev) > len(cur):
            return ""
        prev = cur

    s = topo_sort(graph)
    if s is None:
        return ""
    return "".join(s)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["abc", "ab"], ""),
    ]
    passed = 0
    for words, exp in TESTS:
        got = alien_order(words)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {words} -> {got!r}")
    print(f"\n{passed}/{len(TESTS)} passed")

