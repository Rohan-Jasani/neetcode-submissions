class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set() # row - col
        diag2 = set() # row + col
        path = []
        ans = []
        def dfs( row ):
            if row == n:
                ans.append( [''.join( x ) for x in path] )
                return

            for c in range( n ):
                if c in col or row - c in diag1 or row+c in diag2:
                    continue
                path.append( ['.']*c + ['Q'] + ['.']*(n-c-1) )
                col.add(c)
                diag1.add( row - c )
                diag2.add( row + c )

                dfs( row + 1 )
                
                diag2.remove( row + c )
                diag1.remove( row - c )
                col.remove( c )
                path.pop()
        dfs(0)
        return ans
