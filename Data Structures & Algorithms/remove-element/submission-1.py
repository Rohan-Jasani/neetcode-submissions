class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
        return k
        '''
        n = len( nums )
        ans = 0
        for i, num in enumerate( nums ):
            if num == val: nums[i] = float( 'inf' )
            else: ans+=1
        nums.sort()
        return ans
        '''