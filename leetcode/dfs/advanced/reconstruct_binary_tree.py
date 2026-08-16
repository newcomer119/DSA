class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_recursive(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree_recursive(preorder[1 : mid + 1], inorder[:mid])
    root.right = build_tree_recursive(preorder[mid + 1 :], inorder[mid + 1 :])
    return root


def construct_binary_tree(preorder, inorder):
    return build_tree_recursive(preorder, inorder)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], "3 9 x x 20 15 x x 7 x x"),
        ([1, 2, 3], [2, 1, 3], "1 2 x x 3 x x"),
    ]
    passed = 0
    for pre, ino, exp in TESTS:
        got = " ".join(format_tree(construct_binary_tree(pre, ino)))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] reconstruct -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
