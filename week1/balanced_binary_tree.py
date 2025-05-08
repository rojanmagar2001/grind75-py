from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Top-down (Naive Recursive): At each node we recursively check if left and right subtrees are balanced,
        # compute heights of left and right subtrees and check if the height difference is <= 1.
        # def height(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0
        #     return max(height(node.left), height(node.right)) + 1

        # if not root:
        #     return True

        # left_balanced = self.isBalanced(root.left)
        # right_balanced = self.isBalanced(root.right)
        # height_diff = abs(height(root.left) - height(root.right)) <= 1

        # return left_balanced and right_balanced and height_diff

        # Post-Order Traversal: We can use recursion to compute the height of each subtree and simultaneously
        # check if it's balanced. If any subtree is unbalanced, we propagate a signal (like -1) up the call stack.
        def check(node: Optional[TreeNode]) -> int:
            if not node:
                return 0 # Height of empty tree is 0

            left_height = check(node.left)
            if left_height == -1:
                return -1 # Left Subtree is not balanced

            right_height = check(node.right)
            if right_height == -1:
                return -1 # Right Subtree is not balanced

            if abs(left_height - right_height) > 1:
                return -1 # Current node is not balanced

            return max(left_height, right_height) + 1

        return check(root) != -1
