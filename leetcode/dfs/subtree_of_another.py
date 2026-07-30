class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(tree1,tree2):
    # if tree1 is None and tree2 is None:
    #     return True
    # if tree1 is None or tree2 is None:
    #     return False

    # return (tree1.val == tree2.val and is_same_tree(tree1.left,tree2.left) and is_same_tree(tree1.right, tree2.right))

    if tree1 is None and tree2 is None:
        return True 
    if tree1 is None or tree2 is None:
        return False

    return (tree1.val == tree2.val and is_same_tree(tree1.left,tree2.left) and is_same_tree(tree1.right, tree2.right))


def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    if sub_root is None:
        return True

    if root is None:
        return False

    return (is_same_tree(root,sub_root) or subtree_of_another_tree(root.left,sub_root) or subtree_of_another_tree(root.right, sub_root))
    # if sub_root is None:
    #     return True
    # if root is None:
    #     return False
    # return (is_same_tree(root,sub_root) or subtree_of_another_tree(root.left,sub_root) or subtree_of_another_tree(root.right, sub_root))

        

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
        (["1", "2", "x", "x", "3", "x", "x"], ["2", "x", "x"], True),
        (["1", "2", "x", "x", "3", "x", "x"], ["4", "x", "x"], False),
        (["1", "x", "x"], ["x"], True),
    ]
    passed = 0
    for root_t, sub_t, exp in TESTS:
        root = build_tree(iter(root_t), int)
        sub = build_tree(iter(sub_t), int)
        got = subtree_of_another_tree(root, sub)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] subtree check -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
