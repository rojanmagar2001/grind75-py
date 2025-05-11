# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass

    # ✅ Recursive Approach
    # 🔁 How It Works:
    # Compares the left and right subtrees in a mirrored way:
    # left.left with right.right
    # left.right with right.left
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)

    # 🔁 Iterative Approach (Using Queue)
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue

            if not t1 or not t2 or t1.val != t2.val:
                return False

            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
