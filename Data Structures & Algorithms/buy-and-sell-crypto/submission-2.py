class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        min_price = nums[0]
        profit = 0
        for num in nums:
            profit = max( profit, num - min_price )
            min_price = min( num, min_price )
        return profit
        '''
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range( 1, n ):
            prefix.append( min( nums[i], prefix[-1] ) )
            suffix.append( max( nums[n-i-1], suffix[-1] ) )
        # print( prefix )
        # print( suffix )

        return max( suffix[n-1-i] - prefix[i] for i in range( n ) )
        '''