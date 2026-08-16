class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    def check(node):
        if node is None:
            return (True, -1)

        left_ok, left_h = check(node.left)
        right_ok, right_h = check(node.right)
        balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
        return(balanced, max(left_h, right_h) + 1) 

    return check(tree)[0]
    # def check(node):
    #     if node is None:
    #         return (True, -1)

    #     left_ok,left_h = check(node.left)
    #     right_ok,right_h = check(node.right)
    #     balanced = left_ok and right_ok and abs(left_h - right_h) <= 1

    #     return (balanced, max(left_h,right_h) + 1)
    # return check(tree)[0]

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
        (["1", "2", "x", "x", "3", "x", "x"], True),
        (["1", "2", "3", "4", "x", "x", "x", "x", "x", "x"], False),
        (["x"], True),
    ]
    passed = 0
    for tokens, exp in TESTS:
        tree = build_tree(iter(tokens), int)
        got = is_balanced(tree)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] balanced={got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")
