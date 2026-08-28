# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    @staticmethod
    def reverse_ll( head ):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        heads = [head]
        isComplete = False
        while curr:
            for i in range(0, k-1):
                curr = curr.next
                if curr is None: break

            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt               
                if curr is None: isComplete = True
                else: heads.append( curr )
        # print( isComplete, [x.val for x in heads] )
        n = len( heads )
        end = n if isComplete else n-1
        ans = [heads[-1]]*n
        for i in range( 0, end ):
            ans[i] = self.reverse_ll( heads[i] )
        for i in range( 0, n-1 ):
            heads[i].next = ans[i+1]
        return ans[0]

        

            
        

        