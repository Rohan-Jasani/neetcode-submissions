class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {
            num:num
            for num in nums
        }
        set_nums = set( nums )
        
        def merge( a, b ):
            a = find( a )
            b = find( b )

            if a==b: return False
            else: parent[b] = a

        def find( num ):
            if parent[num]!=num:
                parent[num] = find( parent[num] )

            return parent[num]
        
        for num in set_nums:
            if num + 1 in set_nums: merge( num, num + 1 )
            if num - 1 in set_nums: merge( num - 1, num )

        freq = {}
        max_freq = 0
        for num in set_nums:
            key = find( num )
            f = freq.get( key, 0 )
            freq[ key ] = f + 1
            max_freq = max( max_freq, f + 1 )
        
        return max_freq

            
            

