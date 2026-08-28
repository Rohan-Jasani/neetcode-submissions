# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        q = deque()
        q.append( root )
        depth = 0
        while q:
            # print( depth, q )  
            depth += 1
            for _ in range( len(q) ):
                node = q.popleft()
                if node.left is not None: q.append( node.left )
                if node.right is not None: q.append( node.right )

        return depth

        '''
        def dfs( node ):
            if node is None: return 0
            return 1 + max( dfs(node.left), dfs( node.right ) )
        
        return dfs( root )
        '''