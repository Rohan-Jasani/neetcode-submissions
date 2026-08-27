class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            sum2 = nums[i] + nums[j]
            if sum2 == target: return[i+1, j+1]
            elif sum2 > target: j-=1
            else: i+=1
        return[]