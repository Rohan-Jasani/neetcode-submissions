class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len( nums )
        # pref[i] = a0x...xa[i-1]
        prefix = [1]
        for num in nums:
            prefix.append( num*prefix[-1] )
        
        suffix = [1]
        for num in nums[-1::-1]:
            suffix.append( num*suffix[-1] )
        
        ans = [0]*n
        for i in range( 0, n ):
            ans[i] = prefix[i]*suffix[n-i-1]
        # print( prefix )
        # print( suffix )
        return ans
        '''
        n = len( nums )
        zeros = []
        total = 1
        for i, num in enumerate( nums ):
            if num == 0: zeros.append( i )
            else: total *= num
        
        if len(zeros) > 1: return [0]*n
        elif len( zeros ) == 1:
            ans = [0]*n
            ans[zeros[0]] = total
            return ans
        else:
            return [ total//num for num in nums ]
        '''
