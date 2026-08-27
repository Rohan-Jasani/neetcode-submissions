# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        slow = head
        fast = head
        while True:
            slow = slow.next
            if fast.next is None: return False
            fast = fast.next
            if fast.next is None: return False
            fast = fast.next
            if slow == fast: return True

        return False