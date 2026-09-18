from collections import deque

def count_communication_groups(n, connections):
    adj = [[] for _ in range(n)]
    for a, b in connections:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()
    groups = 0

    for node in range(n):
        if node in visited:
            continue
        visited.add(node)
        groups += 1
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return groups   

def run_tests():

    tests = [
        # Test 1
        (
            5,
            [[0, 1], [1, 2], [3, 4]],
            2
        ),

        # Test 2
        (
            6,
            [[0, 1], [1, 2], [2, 0], [3, 4]],
            3
        ),

        # Test 3 - all connected
        (
            4,
            [[0, 1], [1, 2], [2, 3]],
            1
        ),

        # Test 4 - no connections
        (
            5,
            [],
            5
        ),

        # Test 5 - single station
        (
            1,
            [],
            1
        ),

        # Test 6 - two separate groups
        (
            6,
            [[0, 1], [0, 2], [3, 4], [4, 5]],
            2
        ),

        # Test 7 - cycles
        (
            7,
            [
                [0, 1],
                [1, 2],
                [2, 0],
                [3, 4],
                [4, 5],
                [5, 3]
            ],
            3
        )
    ]

    passed = 0

    for i, (n, connections, expected) in enumerate(tests, 1):

        result = count_communication_groups(n, connections)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED "
                f"(expected {expected}, got {result})"
            )

    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
