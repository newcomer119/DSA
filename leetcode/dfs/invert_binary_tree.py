class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    if tree is None:
        return None
    return Node(tree.val, invert_binary_tree(tree.right), invert_binary_tree(tree.left))


# --- Daily tests ---
if __name__ == "__main__":
    def build(tokens):
        it = iter(tokens)
        def helper():
            val = next(it)
            if val == "x":
                return None
            return Node(int(val), helper(), helper())
        return helper()

    def key(node):
        if node is None:
            return "x"
        return f"{node.val} {key(node.left)} {key(node.right)}"

    root = build(["1", "2", "x", "x", "3", "x", "x"])
    got = invert_binary_tree(root)
    ok = key(got) == "1 3 x x 2 x x"
    print(f"[{'PASS' if ok else 'FAIL'}] invert tree -> {key(got)}")
    back = invert_binary_tree(got)
    ok2 = key(back) == "1 2 x x 3 x x"
    print(f"[{'PASS' if ok2 else 'FAIL'}] double invert restores tree")
    print(f"\n{(1 if ok else 0) + (1 if ok2 else 0)}/2 passed")