class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len( board )
        n = len( board[0] )
        
        seen = set()
        def dfs( r, c, i ):
            if i == len( word ): return True
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in seen or board[r][c] != word[i]: return False
            seen.add( ( r, c ) )
            found = dfs( r-1, c, i+1 ) or dfs( r+1, c, i+1 ) or dfs( r, c-1, i+1 ) or dfs( r, c+1, i+1 )
            seen.remove( ( r, c ) )
            return found

        for j in range( m*n ):
            # coord = j//n, j%n
            if dfs( j//n, j%n, 0 ): return True
        return False
            


