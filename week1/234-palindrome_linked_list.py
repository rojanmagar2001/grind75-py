# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a
# or false otherwise.
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass

    def isPalindromeNaive(self, head: Optional[ListNode]) -> bool:
        # ✅ A naive approach using extra space (O(n) time, O(n) space)
        vals: List[ListNode] = []
        current = head

        while current:
            vals.append(current.val)
            current = current.next

        return vals == vals[::-1]

    def isPalindromeOptimized(self, head: Optional[ListNode]) -> bool:
        # ⚙️ Optimized Approach – Reverse second half (O(1) space)

        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Step 3: Compare the first half and reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
