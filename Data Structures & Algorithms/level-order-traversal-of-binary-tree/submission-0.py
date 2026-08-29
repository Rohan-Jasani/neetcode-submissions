# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        result = []
        def bfs( node ):
            q = deque([node])
            while q:
                level = []
                for _ in range( len(q) ):
                    u =  q.popleft()
                    level.append(u.val)
                    if u.left:  q.append( u.left )
                    if u.right: q.append( u.right )
                result.append(level)
        bfs(root)
        return result

