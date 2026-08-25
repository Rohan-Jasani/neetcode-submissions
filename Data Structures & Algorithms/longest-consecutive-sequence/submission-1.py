class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set( nums )
        ans = 0
        for num in nums:
            if num-1 in nums: continue
            
            length = 1

            while num + length in nums:
                length += 1
            
            ans = max( ans, length )
        return ans

        '''
        set_nums = set( nums )
        parent = {
            num:num
            for num in nums
        }
        
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
        '''

            
            

