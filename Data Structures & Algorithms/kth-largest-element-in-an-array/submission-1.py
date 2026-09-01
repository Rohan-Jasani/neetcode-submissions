import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify( heap )
        for num in nums[k:]:
            heapq.heappush( heap, num )
            heapq.heappop( heap )
        
        return heapq.heappop( heap )