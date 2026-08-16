class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root: Node, node1: Node, node2: Node) -> Node:
    if not root:
        return None 
    if root in (node1, node2):
        return root 
    left = lca(root.left,node1,node2)
    right = lca(root.right,node1,node2)
    if left and right:
        return root 
    if left:
        return left 
    if right:
        return right 
    return None 
    

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def find_node(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)

    return find_node(root.left, target) or find_node(root.right, target)


# --- Daily tests ---
if __name__ == "__main__":
    tokens = ["3", "5", "6", "x", "x", "2", "7", "x", "x", "4", "x", "x", "1", "0", "x", "x", "8", "x", "x"]
    root = build_tree(iter(tokens), int)
    TESTS = [(5, 1, 3), (5, 4, 5), (6, 4, 5)]
    passed = 0
    for v1, v2, exp in TESTS:
        ans = lca(root, find_node(root, v1), find_node(root, v2))
        got = ans.val if ans else None
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] LCA({v1},{v2}) -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
