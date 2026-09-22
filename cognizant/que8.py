def can_restore_all(n, dependencies):

    prereq = {i: [] for i in range(n)}

    for a, b in dependencies:
        prereq[a].append(b)

    cycle = set()
    visited = set()

    def dfs(node):

        if node in cycle:
            return False

        if node in visited:
            return True

        cycle.add(node)

        for pre in prereq[node]:
            if not dfs(pre):
                return False

        cycle.remove(node)
        visited.add(node)

        return True

    for node in range(n):
        if not dfs(node):
            return False

    return True

# =============================================
# TEST CASES - DO NOT MODIFY
# =============================================

def run_tests():

    tests = [
        # Simple chain
        (
            4,
            [[1, 0], [2, 1], [3, 2]],
            True
        ),

        # Cycle
        (
            3,
            [[1, 0], [2, 1], [0, 2]],
            False
        ),

        # Multiple dependencies
        (
            5,
            [[1, 0], [2, 0], [3, 1], [3, 2]],
            True
        ),

        # No dependencies
        (
            5,
            [],
            True
        ),

        # Two-node cycle
        (
            2,
            [[1, 0], [0, 1]],
            False
        ),

        # Disconnected components, no cycle
        (
            6,
            [[1, 0], [2, 1], [4, 3]],
            True
        ),

        # Cycle in only one component
        (
            6,
            [[1, 0], [2, 1], [4, 3], [5, 4], [3, 5]],
            False
        ),

        # Diamond dependency
        (
            4,
            [[1, 0], [2, 0], [3, 1], [3, 2]],
            True
        ),

        # Longer cycle
        (
            5,
            [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]],
            False
        ),

        # Single station
        (
            1,
            [],
            True
        ),
    ]

    passed = 0

    for i, (n, dependencies, expected) in enumerate(tests, 1):

        result = can_restore_all(n, dependencies)

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