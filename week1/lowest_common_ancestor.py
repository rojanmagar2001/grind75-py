# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode | None:
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left # LCA must be in the left sub tree
            elif p.val > current.val and q.val > current.val:
                current = current.left
            else:
                return current

        return None
