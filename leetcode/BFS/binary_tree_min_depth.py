from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    if root is None:
        return 0
    queue = deque([root])
    depth = -1

    while len(queue)  > 0:
        n = len(queue)
        depth += 1
        for _ in range(n):
            node = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

                
    
    return depth

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
        (["1", "x", "x"], 0),
        (["1", "2", "x", "x", "x", "x", "x"], 1),
        (["1", "x", "2", "x", "3", "x", "x"], 2),
    ]
    passed = 0
    for tokens, exp in TESTS:
        root = build_tree(iter(tokens), int)
        got = binary_tree_min_depth(root)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] min depth -> {got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")
