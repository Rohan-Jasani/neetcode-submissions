# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse the second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge the two halves
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

    
    '''    
        iter2 = head
        nodes = [head]
        while iter2.next is not None:
            iter2 = iter2.next
            nodes.append( iter2 )
        n = len( nodes )
        result = [None]*n
        for i in range(n):
            if i & 1:
                result[i] = nodes[ n - (i+1)//2 ]
            else:
                result[i] = nodes[i//2]
        
        # print( [x.val for x in result] )
        for i in range( n-1 ):
            result[i].next = result[i+1]
        result[n-1].next = None
    '''
        
        
        