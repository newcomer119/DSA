class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p: int, q: int) -> int:
    # if p < bst.val and q < bst.val:
    #     return lca_on_bst(bst.left,p,q)

    # elif p > bst.val and q > bst.val:
    #     return lca_on_bst(bst.right,p,q)

    # else:
    #     return bst.val 


    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p ,q)

    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p ,q)

    else:
        return bst.val
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
    tokens = ["6", "2", "1", "x", "x", "4", "3", "x", "x", "5", "x", "x", "8", "7", "x", "x", "9", "x", "x"]
    bst = build_tree(iter(tokens), int)
    TESTS = [(2, 8, 6), (2, 4, 2), (3, 5, 4)]
    passed = 0
    for p, q, exp in TESTS:
        got = lca_on_bst(bst, p, q)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] LCA({p},{q}) -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
