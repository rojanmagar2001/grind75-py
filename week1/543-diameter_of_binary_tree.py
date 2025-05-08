from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS Approach
        # 🔍 How it works:
        # For each node, left + right is the path passing through it.
        # The return 1 + max(left, right) gives the height to the parent.
        # We update a max_diameter variable along the way.
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right)

            # return the height
            return 1 + max(left, right)

        dfs(root)

        return self.max_diameter
