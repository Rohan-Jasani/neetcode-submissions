
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def bsearch(l, r):
            if l > r:
                return False

            mid = (l + r) // 2

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                return bsearch(mid + 1, r)
            else:
                return bsearch(l, mid - 1)

        return bsearch(0, m * n - 1)

        '''
        m = len( matrix )
        n = len( matrix[0] )

        def add_tup( t1, t2 ):
            num1 = n*t1[0] + t1[1]
            num2 = n*t2[0] + t2[1]
            total = num1 + num2
            return ( total//n, total%n )
        
        def div_tup( t, div ):
            num = n*t[0] + t[1]
            ans = num//div
            return ( ans//n, ans%n )

        def bsearch( l, r ):
            if l > r:  return False

            mid = div_tup( add_tup( l, r ), 2 )
            mid_val = matrix[mid[0]][mid[1]]
            if mid_val == target: return True
            elif mid_val < target: return bsearch( add_tup( mid, ( 0, 1) ), r )
            else: return bsearch( l, add_tup( mid, ( 0, -1 ) ) )
        
        return bsearch( (0,0), ( m-1, n-1 ) )
        '''



