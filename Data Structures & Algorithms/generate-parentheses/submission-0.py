class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []

        def dfs( open_b, closed_b ):
            if open_b + closed_b == 2*n:
                ans.append( ''.join(path) )
            
            # open bracked
            if open_b < n:
                path.append( '(' )
                dfs( open_b + 1, closed_b )
                path.pop()

            if closed_b < open_b:
                path.append( ')' )
                dfs( open_b, closed_b + 1 )
                path.pop()
        
        dfs( 0, 0 )
        return ans

