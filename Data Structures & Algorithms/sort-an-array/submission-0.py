class Solution:
    @staticmethod
    def sortArray(nums: List[int]) -> List[int]:
        n = len( nums )
        if n <= 1: return nums
        mid = n>>1
        left = Solution.sortArray( nums[:mid] )
        right = Solution.sortArray( nums[mid:] )
        result = []
        i = 0
        j = 0
        while i < len( left ) and j < len( right ):
            if left[i] <= right[j]: 
                result.append( left[i] )
                i += 1
            else: 
                result.append( right[j] )
                j += 1

        result += left[i:]
        result += right[j:]
        return result