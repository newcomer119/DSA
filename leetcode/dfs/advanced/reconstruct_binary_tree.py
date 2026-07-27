class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_recursive(preorder,preorder_index,inorder_start,size,value_to_index):
    if size <= 0:
        return None

    root_value = preorder[preorder_index]
    inorder_root_index = value_to_index[root_value]
    left_subtree_size = inorder_root_index - inorder_start

    left_child = build_tree_recursive(preorder,preorder_index + 1, inorder_start, left_subtree_size, value_to_index)
    right_child = build_tree_recursive(preorder, preorder_index + 1 + left_subtree_size,inorder_root_index + 1, size - 1 - left_subtree_size, value_to_index)


    return Node(root_value,left_child,right_child)
    
def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Node:
    value_to_index = {val : idx for idx,val in enumerate(inorder)}
    return build_tree_recursive(preorder,0,0,len(preorder),value_to_index)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

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
