# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build_subtree( self, root ):
        subtree = defaultdict( int )
        def dfs( node ):
            if node is None: return 0
            subtree[node] = 1
            subtree[node] += dfs( node.left )
            subtree[node] += dfs( node.right )
            return subtree[node]
        dfs( root )
        return subtree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        subtree = self.build_subtree( root )

        def find( node, k ):
            
            if k==0: return node
            left = subtree[node.left]
            # print( node.val, k, left )
            if left == k-1: return node
            elif left > k - 1: return find( node.left, k )
            elif left < k-1: return find( node.right, k -left - 1 )
        
        return find( root, k ).val
        
