# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        size = 1
        while fast.next: 
            size+=1
            fast = fast.next
        fast = head
        print( size )
        if size == n: return head.next
        for _ in range( n ):
            fast = fast.next
        
        while fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next
            size+=1
        slow.next = slow.next.next
        return head
        