from heapq import heappush, heappop

def minimum_travel_time(n, roads):
    adj = [[] for _ in range(n)]
    
    for u,v, weight in roads:
        adj[u].append((v,weight))
        adj[v].append((u,weight))


    minheap = [(0,0)]
    visited = set()

    while minheap:  
        distance,node = heappop(minheap)
        if node in visited:
            continue

        visited.add(node)

        if node == n- 1:
            return distance 

        for neighbor,weight in adj[node]:
            if neighbor not in visited:
                heappush(minheap, (distance + weight, neighbor))

    return -1          

def run_tests():

    tests = [
        (
            5,
            [
                [0, 1, 4],
                [0, 2, 1],
                [2, 1, 2],
                [1, 3, 1],
                [2, 3, 5],
                [3, 4, 3]
            ],
            7
        ),

        (
            4,
            [[0, 1, 5], [1, 2, 2]],
            -1
        ),

        (
            3,
            [[0, 1, 10], [0, 2, 100], [1, 2, 5]],
            15
        ),

        # Direct route is best
        (
            3,
            [[0, 1, 10], [1, 2, 10], [0, 2, 5]],
            5
        ),

        # Single warehouse
        (
            1,
            [],
            0
        ),

        # Several possible routes
        (
            6,
            [
                [0, 1, 2],
                [0, 2, 8],
                [1, 2, 3],
                [1, 3, 5],
                [2, 4, 1],
                [3, 5, 4],
                [4, 5, 2]
            ],
            8
        ),

        # Disconnected
        (
            5,
            [[0, 1, 1], [2, 3, 1], [3, 4, 1]],
            -1
        ),

        # Large edge weights
        (
            4,
            [
                [0, 1, 1000000000],
                [1, 3, 1000000000],
                [0, 2, 5],
                [2, 3, 5]
            ],
            10
        ),

        # Multiple routes to same node
        (
            4,
            [
                [0, 1, 10],
                [0, 2, 1],
                [2, 1, 1],
                [1, 3, 1],
                [2, 3, 20]
            ],
            3
        ),
    ]

    passed = 0

    for i, (n, roads, expected) in enumerate(tests, 1):
        result = minimum_travel_time(n, roads)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(
                f"Test {i}: FAILED | "
                f"expected={expected}, got={result}"
            )

    print(f"\nRESULT: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()