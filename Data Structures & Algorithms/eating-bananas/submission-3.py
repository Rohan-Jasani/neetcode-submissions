class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        min_v = math.ceil( sum( piles )/h )
        max_v = max( piles )

        def bsearch( l, r ):
            if l > r: return l

            mid = ( l+r )>>1
            total = sum( math.ceil(x/mid) for x in piles )
            if total <= h: return bsearch( l, mid-1 )
            else: return bsearch( mid+1, r )
        
        return bsearch( min_v, max_v )
        