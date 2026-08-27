# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        iter2 = head
        nodes = [head]
        while iter2.next is not None:
            iter2 = iter2.next
            nodes.append( iter2 )
        n = len( nodes )
        result = [ListNode(0) for _ in range(n)]
        for i in range(n):
            if i & 1:
                result[i] = nodes[ n - (i+1)//2 ]
            else:
                result[i] = nodes[i//2]
        
        # print( [x.val for x in result] )
        for i in range( n-1 ):
            result[i].next = result[i+1]
        result[n-1].next = None
        
        
        