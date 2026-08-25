class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
