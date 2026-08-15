class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    res = []
    def dfs(root):
        if not root:
            res.append(" X ")
            return 
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
        return 
    dfs(root)
    return " ".join(res)

def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == "X":
            return None
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur

    return dfs(iter(s.split()))
    

# --- Daily tests ---
if __name__ == "__main__":
    def build_tree(nodes):
        val = next(nodes)
        if val == "x":
            return None
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur

    def tree_str(root):
        if not root:
            return "x"
        return f"{root.val} {tree_str(root.left)} {tree_str(root.right)}"

    tokens = ["1", "2", "x", "x", "3", "x", "x"]
    root = build_tree(iter(tokens))
    restored = deserialize(serialize(root))
    ok = tree_str(restored) == tree_str(root)
    print(f"[{'PASS' if ok else 'FAIL'}] serialize/deserialize round-trip")
    print(f"\n{1 if ok else 0}/1 passed")
