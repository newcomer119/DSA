class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> list[str]:
    # def dfs(root,path,res):
    #     if not root:
    #         return 
    #     if all (c is None for c in root.children):
    #         res.append("->".join(path + [str(root.val)]))
    #         return 
    
    #     for child in root.children:
    #         if child is not None:
    #             dfs(child, path + [str(root.val)], res)

    # res = []
    # dfs(root, [], res)
    # return res

    def dfs(root,path,res):
        if not root:
            return 

        if all (c is None for c in root.children):
            res.append("->".join(path + [str(root.val)]))
            return 

        for child in root.children:
            if child is not None:
                dfs(child, path + [str(root.val)], res)
    res = []
    dfs(root, [], res)
    return res


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

    return Node(f(val), children)


# --- Daily tests ---
if __name__ == "__main__":
    root = Node(1, [Node(2), Node(3), Node(4)])
    got = sorted(ternary_tree_paths(root))
    exp = ["1->2", "1->3", "1->4"]
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] paths -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
