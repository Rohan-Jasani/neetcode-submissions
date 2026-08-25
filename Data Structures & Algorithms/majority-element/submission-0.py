class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = nums[0]
        for num in nums:
            if num == ans: count+=1
            elif count == 0: ans = num
            else: count -= 1
        return ans
