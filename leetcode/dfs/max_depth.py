class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    # def dfs(root):
    #     # null node adds no depth
    #     if not root:
    #         return 0
    #     # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
    #     return max(dfs(root.left), dfs(root.right)) + 1
    # return dfs(root) - 1 if root else 0

    def dfs(root):
        if not root:
            return 0

        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) -1 if root else 0

# --- Daily tests ---
if __name__ == "__main__":
    def build_tree(tokens):
        it = iter(tokens)
        def helper():
            val = next(it)
            if val == "x":
                return None
            return Node(int(val), helper(), helper())
        return helper()

    TESTS = [
        (["x"], 0),
        (["1", "x", "x"], 0),
        (["1", "2", "x", "x", "3", "x", "x"], 1),
    ]
    passed = 0
    for tokens, exp in TESTS:
        got = tree_max_depth(build_tree(tokens))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] depth={got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")