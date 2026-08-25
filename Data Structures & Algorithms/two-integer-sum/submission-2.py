from bisect import bisect_left
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len( nums )
        nums = [ ( num, idx ) for idx, num in enumerate( nums ) ]
        nums.sort()

        for num, i_old in nums:
            j_new = bisect_left( nums, ( target - num, 0 ) )
            if j_new < n and i_old!=nums[j_new][1] and nums[j_new][0] == target - num: return [min( i_old, nums[j_new][1] ), max( i_old, nums[j_new][1] ) ]





