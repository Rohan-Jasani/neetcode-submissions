class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board = np.array( board )
        valid = set( [str(i) for i in range( 1, 10 )] )
        valid.add( '.' )
        
        for row in board:
            seen = set()
            for ch in row:
                if ch not in valid: return False
                if ch !='.' and ch in seen: return False
                seen.add( ch )
        
        for i in range( 0, 9 ):
            seen = set()
            for j in range( 0, 9 ):
                ch = board[j][i]
                if ch !='.' and ch in seen: return False
                seen.add( ch )
        seen = {
            ( 0, 0 ): set(),
            ( 0, 1 ): set(),
            ( 0, 2 ): set(),
            ( 1, 0 ): set(),
            ( 1, 1 ): set(),
            ( 1, 2 ): set(),
            ( 2, 0 ): set(),
            ( 2, 1 ): set(),
            ( 2, 2 ): set(),
        }
        for i in range( 0, 9 ):
            for j in range( 0, 9 ):
                key = ( i//3, j//3 )
                ch = board[i][j]
                if ch != '.' and ch in seen[ key ]: return False
                seen[ key ].add( ch )
        return True
        


