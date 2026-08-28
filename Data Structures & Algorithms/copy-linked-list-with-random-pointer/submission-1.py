"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        val_list = []
        next_list = []
        random_list = []
        nd_to_idx = {}
        
        itr = head
        i = 0
        while itr:
            val_list.append( itr.val )
            next_list.append( i+1 )
            nd_to_idx[itr] = i    
            itr = itr.next
            i += 1
        next_list[-1] = None

        random_list = []
        new_nodes = []
        itr = head
        while itr:
            random_list.append( nd_to_idx.get(itr.random, None ) )
            new_nodes.append( Node( itr.val ) )
            itr = itr.next

        # print( val_list  )
        # print( next_list )
        # print( random_list )
        
        for i, nd in enumerate( new_nodes ):
            if ( nx := next_list[i] ) is not None:
                nd.next = new_nodes[nx]
            if ( rd := random_list[i] ) is not None:
                nd.random = new_nodes[rd]
        
        return new_nodes[0]

            