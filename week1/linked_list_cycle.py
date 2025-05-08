from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val: ListNode = x
        self.next: ListNode | None = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycleFloydsCycleDetection(head)

    def hasCycleFloydsCycleDetection(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection Algorithm (Tortoise and Hare) Approach: Using two pointers: slow (1x speed) and fast (2x speed)
        # If there's a cycle, they'll eventually meet.
        # If there's no cycle, fast will reach the end (null).
        # Time: O(n)
        # Space: O(1)
        if not head:
            return False
        slow = fast = head

        while fast and fast.next and slow.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycleHasSetApproach(self, head: Optional[ListNode]) -> bool:
        # Hash Set (Visited Nodes) Approach: We will traverse the list and store visited nodes in a set.
        # If a node is seen again, a cycle exists.
        # Time: O(n)
        # Space: O(n)
        visited = set()

        current = head

        while current:
            if current in visited:
                return True

            visited.add(current)

            current = current.next

        return False
