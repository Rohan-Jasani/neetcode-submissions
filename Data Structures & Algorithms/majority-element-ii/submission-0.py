class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len( nums )
        freq = Counter( nums )
        return [ x for x, f in freq.items() if f > n//3 ]