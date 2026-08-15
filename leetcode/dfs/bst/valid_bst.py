from math import inf 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    # def dfs(root,min_val,max_val):
    #     if not root:
    #         return True

    #     if not (min_val < root.val < max_val):
    #         return False

    #     return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    # return dfs(root,-inf,inf)
        

    def dfs(root,min_val,max_val):
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        return dfs(root.left,min_val, root.val) and dfs(root.right,root.val, max_val)
        
    return dfs(root,-inf,inf)
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
        (["2", "1", "x", "x", "3", "x", "x"], True),
        (["5", "1", "x", "x", "4", "x", "x"], False),
        (["1", "x", "x"], True),
    ]
    passed = 0
    for tokens, exp in TESTS:
        root = build_tree(iter(tokens), int)
        got = valid_bst(root)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] valid={got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")
