# 113. Path Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:
# # Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []
 # Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, remaining, path):
            if (node is None):
                return 
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:
                paths.append(path[:])
            else:
                dfs(node.left,remaining,path)
                dfs(node.right,remaining,path)
            path.pop()

        paths = []
        dfs(root,targetSum, [])
        return paths


# --- Daily tests ---
if __name__ == "__main__":
    def build(tokens):
        it = iter(tokens)
        def helper():
            val = next(it)
            if val == "x":
                return None
            return TreeNode(int(val), helper(), helper())
        return helper()

    sol = Solution()
    root = build(["5", "4", "11", "7", "x", "x", "2", "x", "x", "x", "x", "8", "x", "x"])
    got = sol.pathSum(root, 22)
    ok = got == [[5, 4, 11, 2]]
    print(f"[{'PASS' if ok else 'FAIL'}] pathSum target=22 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")