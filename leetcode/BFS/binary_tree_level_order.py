from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    result = []
    if root is None:
        return result

    queue = deque([root])
    while len(queue)  > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left,node.right]:
                if child is not None:
                    queue.append(child)

        result.append(new_level)
    return result

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

    return Node(f(val), left, right)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["x"], []),
        (["1", "x", "x"], [[1]]),
        (["3", "9", "x", "x", "20", "15", "x", "x", "7", "x", "x"], [[3], [9, 20], [15, 7]]),
    ]
    passed = 0
    for tokens, exp in TESTS:
        root = build_tree(iter(tokens), int)
        got = level_order_traversal(root)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {tokens[0] if tokens[0] != 'x' else 'empty'} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
