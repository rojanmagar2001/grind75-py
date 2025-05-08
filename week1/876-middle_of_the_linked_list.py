from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arrNode: List[ListNode] = []

        current = head

        while current:
            arrNode.append(current)
            current = current.next

        return arrNode[len(arrNode) // 2]
