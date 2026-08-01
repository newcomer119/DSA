# Reconstructing Sequence
# Prereq: Topological Sort

# A sequence s is a list of integers. Its subsequence is a new sequence that can be made up by deleting elements from s, without changing the order of integers.

# We are given an original sequence (which is a permutation of the integers from 1 to n) and a list of subsequences seqs.

# Determine whether original is the only sequence that can be reconstructed from seqs. Reconstruction means building the shortest sequence so that all sequences in seqs are subsequences of it.

# Parameters
# original: a list of integers of size n representing the original sequence.
# seqs: a list of sequences of size m representing the sequences to be reconstructed.
# Result
# true or false, depending on whether the original sequence can be uniquely reconstructed.
# Examples
# Example 1:
# Input: original: [1,2,3], seqs: [[1,2], [1,3]]

# Output: false

# Explanation:

# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

# Example 2:
# Input: original: [1,2,3], seqs: [[1,2]]

# Output: false

# Explanation:

# There is only one subsequence, so the reconstructed original sequence can only be [1,2] which is missing 3.

# Example 3:
# Input: orginal: [1,2,3], seqs: [[1,2], [1,3], [2,3]]

# Output: true

# Explanation:

# [1,2,3] is the only sequence that can be reconstructed from [1,2], [1,3], and [2,3].

# Example 4:
# Input: original: [4,1,5,2,6,3], seqs: [[5,2,6,3], [4,1,5,2]]

# Output: true

# Explanation:

# [4,1,5,2,6,3] is the only sequence that can be reconstructed from [[5,2,6,3], [4,1,5,2]].

# Constraints
# 1 <= n <= 10^4
# 1 <= m <= 10^4
# 1 <= len(seqs[i]) <= n

from collections import deque

def sequence_reconstruction(original: list[int], seqs: list[list[int]]) -> bool:
    def find_indegree(graph):
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        return indegree
   
    # def find_indegree(graph):
    #     indegree = {node : 0 for node in graph}
    #     for node in graph:
    #         for neighbor in graph[node]:
    #             indegree[neighbor] += 1
    #     return indegree
    def topo_sort(graph):
        order = []
        queue =deque()
        indegree = find_indegree(graph)

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            if len(queue) > 1:
                return False

            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(order) == len(original) and order == original

    
    # def topo_sort(graph):
    #     order = []
    #     queue = deque()
    #     indegree = find_indegree(graph)

    #     for node in indegree:
    #         if indegree[node] == 0:
    #             queue.append(node)

    #     while queue:
    #         if len(queue) > 1:
    #             return False
    #         node = queue.popleft()
    #         order.append(node)
    #         for neighbor in graph[node]:
    #             indegree[neighbor] -= 1
    #             if indegree[neighbor] == 0:
    #                 queue.append(neighbor)
    #     return len(order) == len(original) and order == original
        
    n = len(original)
    graph = {node : set() for node in range(1, 1 + n)}
    for seq in seqs:
        for i in range(len(seq) - 1):
            source,destination = seq[i] , seq[i + 1]
            graph[source].add(destination)

    return topo_sort(graph)
    # n = len(original)
    # graph = {node : set() for node in range(1, 1 + n)}
    # for seq in seqs:
    #     for i in range(len(seq) - 1):
    #         source , destination = seq[i], seq[i + 1]
    #         graph[source].add(destination)
    # return topo_sort(graph)

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3], [[1, 2], [1, 3]], False),
        ([1, 2, 3], [[1, 2], [1, 3], [2, 3]], True),
        ([1, 2, 3], [[1, 2]], False),
        ([4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]], True),
    ]
    passed = 0
    for original, seqs, exp in TESTS:
        got = sequence_reconstruction(original, seqs)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {original} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
