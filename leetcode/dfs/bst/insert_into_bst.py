class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
    # if bst is None:
    #     return Node(val)
    # if bst.val < val:
    #     bst.right = insert_bst(bst.right,val)
    # elif bst.val > val:
    #     bst.left = insert_bst(bst.left,val)
    # return bst        
    if bst is None:
        return Node(val)

    if bst.val < val:
        bst.right = insert_bst(bst.right,val)
    elif bst.val > val:
        bst.left = insert_bst(bst.left,val)
    return bst

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

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
        (["2", "1", "x", "x", "3", "x", "x"], 4, "2 1 x x 3 x 4 x x"),
        (["x"], 1, "1 x x"),
    ]
    passed = 0
    for tokens, val, exp in TESTS:
        bst = build_tree(iter(tokens), int)
        got = " ".join(format_tree(insert_bst(bst, val)))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] insert {val} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
