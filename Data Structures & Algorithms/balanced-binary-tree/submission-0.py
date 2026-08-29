# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def h( node ):
            nonlocal isBalanced
            
            if node is None: return -1
            l = h( node.left )
            if l == -2: return -2
            r = h( node.right )
            if r== -2: return -2

            if abs( r-l ) > 1: 
                isBalanced = False
                return -2
            return 1 + max( l, r )
        print( h( root ) )
        return isBalanced