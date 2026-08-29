# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs( node ):
            if node is None: 
                preorder.append( '#' )
                return
            preorder.append( str( node.val ) )
            dfs( node.left )
            dfs( node.right )
        dfs( root )
        print( preorder )
        return ','.join( preorder )
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split( ',' )
        index = 0
        def build():
            nonlocal index
            value = preorder[index]
            index += 1
            if value == '#': return None

            node = TreeNode( int( value ) )
            node.left = build()
            node.right = build()

            return node
        return build()