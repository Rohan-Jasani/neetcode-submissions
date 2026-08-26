class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # convert the array to:
        # idx: 0, 1, 2, 3, 4, 5,...,n-1
        # arr: 1, 2, 3, 4, 5, 6,..., n
        
        n = len( nums )
        for i in range(0, n):
            while 1 <= nums[i] <= n and nums[i] != nums[ ( j := nums[i] - 1 ) ]:
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        
        for i in range( 0, n ):
            if nums[i] != i + 1: return i+1
        return n+1