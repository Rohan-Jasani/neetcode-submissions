from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter( nums )
        freq_map = [ (f, num) for num, f in freq_map.items() ]
        freq_map.sort( reverse = True )
        return [ num for f, num in freq_map[:k]]