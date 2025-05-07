from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # reate a dummy node to simplify the code
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists and compare nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach any remaining nodes from either list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
