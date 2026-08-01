from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> list[int]:
    # res = []
    # if root is None:
    #     return res
    # queue = deque([root])
    # while len(queue) > 0:
    #     n = len(queue)
    #     res.append(queue[0].val) # right most node 

    #     for _ in range(n):
    #         node = queue.popleft()
    #         if node.right is not None:
    #             queue.append(node.right)
    #         if node.left is not None:
    #             queue.append(node.left)
    # return res

    res= []
    if root is None:
        return res

    queue =deque([root])
    while queue:
        n = len(queue)
        res.append(queue[0].val)

        for _ in range(n):
            node = queue.popleft()
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
    return res
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)



# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["1", "x", "x"], [1]),
        (["1", "2", "x", "5", "x", "x", "3", "x", "4", "x", "x"], [1, 3, 4]),
        (["1", "x", "2", "x", "3", "x", "x"], [1, 2, 3]),
    ]
    passed = 0
    for tokens, exp in TESTS:
        root = build_tree(iter(tokens), int)
        got = binary_tree_right_side_view(root)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] right view -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
