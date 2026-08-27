class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        n = len( nums )
        for fast in range( 1, n ):
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1 

        return slow
                
