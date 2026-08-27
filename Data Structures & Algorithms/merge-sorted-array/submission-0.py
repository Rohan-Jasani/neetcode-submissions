class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for j, num in enumerate( nums2 ):
            while i < m + j and nums1[i] < num: i+=1
            for k in range( m + j, i, -1 ):
                nums1[k], nums1[k-1] = nums1[k-1], nums1[k]
            nums1[i] = num
        