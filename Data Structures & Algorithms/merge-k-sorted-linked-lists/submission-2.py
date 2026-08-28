# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def min_ll( itrs ):
#     k = len( itrs )
#     min_idx = -1
#     min_val = float( 'inf' )
#     for idx in range( 0, k ):
#         nd = itrs[idx]
#         if nd is None: continue
#         val = nd.val
#         if val <= min_val:
#             min_idx = idx
#             min_val = val
#     return min_idx
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, nd in enumerate( lists ):
            if nd:
                heapq.heappush( heap, ( nd.val, i, nd ) )
        dummy = ListNode( )
        curr = dummy
        while heap:
            val, i, nd = heapq.heappop(heap)
            nxt = nd.next
            if nxt:
                heapq.heappush( heap, (nxt.val, i, nxt ) )
            curr.next = nd
            curr = curr.next
        
        return dummy.next
        '''
        # count_none = 0
        # for i in lists:
        #     if i is None:
        #         count_none+=1
        k = len( lists )
        itrs = lists
        dummy = ListNode()
        curr = dummy
        while True:
            idx = min_ll( itrs )
            if idx == -1: break
            curr.next = itrs[idx]
            curr = curr.next
            itrs[ idx ] = itrs[ idx ].next
            # if itrs[idx] is None: count_none += 1
        
        return dummy.next
        '''

            



