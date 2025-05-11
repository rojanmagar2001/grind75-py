
# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted
# in ascending order, convert it to a height-balanced binary search tree.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert_to_bst(left_index: int, right_index: int):
            # Base case: If the left index is greater than the right index,
            # the subarray is empty, and there is no tree to construct.
            if left_index > right_index:
                return None

            # Choosing the middle element of the subarray to be the root of the BST.
            middle_index = (left_index + right_index) // 2
            left_subtree = convert_to_bst(left_index, middle_index - 1)
            right_subtree = convert_to_bst(middle_index + 1, right_index)

            return TreeNode(nums[middle_index], left_subtree, right_subtree)

        return convert_to_bst(0, len(nums) - 1)
