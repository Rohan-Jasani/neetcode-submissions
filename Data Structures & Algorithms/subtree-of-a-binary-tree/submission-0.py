# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    @staticmethod
    def isSame( a, b ):
        if a is None or b is None: return a==b
        if a.val != b.val: return False
        return Solution.isSame( a.left, b.left ) and Solution.isSame( a.right, b.right )
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: return True
        if root is None: return False

        if Solution.isSame( root, subRoot ): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        