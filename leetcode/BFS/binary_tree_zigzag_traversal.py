from collections import deque 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> list[list[int]]:
    res = []
    if root is None:
        return res
    queue = deque([root])
    left_to_right = True

    while len(queue) > 0:
        n = len(queue)
        new_level = deque()
        for _ in range(n):
            node =  queue.popleft()
            if left_to_right:
                new_level.append(node.val)
            else:
                new_level.appendleft(node.val)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
                
        res.append(list(new_level))
        left_to_right = not left_to_right        
        
    return res

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
        (["1", "x", "x"], [[1]]),
        (["3", "9", "x", "x", "20", "15", "x", "x", "7", "x", "x"], [[3], [20, 9], [15, 7]]),
        (["1", "2", "x", "x", "3", "x", "x"], [[1], [3, 2]]),
    ]
    passed = 0
    for tokens, exp in TESTS:
        root = build_tree(iter(tokens), int)
        got = zig_zag_traversal(root)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] zigzag -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
