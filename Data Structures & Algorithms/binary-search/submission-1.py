from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        0,1,2,5
        def bsearch( l, r ):
            if l > r: return -1

            mid = (l+r)>>1
            if target == nums[mid]: return mid
            elif target > nums[mid]: return bsearch( mid+1, r )
            elif target < nums[mid]: return bsearch( l, mid - 1 )
        
        ans = bsearch( 0, n-1 )
        return ans if nums[ans]==target else -1
        '''
        idx = bisect_left( nums, target )
        return idx if nums[idx] == target else -1
        '''