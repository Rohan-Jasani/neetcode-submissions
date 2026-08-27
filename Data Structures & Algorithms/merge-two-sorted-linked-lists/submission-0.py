# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode( -101 )
        curr = dummy
        iter1 = list1
        iter2 = list2
        while iter1 and iter2:
            if iter1.val <= iter2.val:
                curr.next = iter1
                iter1 = iter1.next
            else:
                curr.next = iter2
                iter2 = iter2.next
            curr = curr.next
        if iter1 is None    : curr.next = iter2
        elif iter2 is None  : curr.next = iter1

        return dummy.next


