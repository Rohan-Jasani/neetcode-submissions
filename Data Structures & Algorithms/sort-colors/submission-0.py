class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        lo = 0 # 0 to lo-1 are 0s
        mid = 0 # lo to mid - 1 are 1s
        hi = n - 1 # high+1 to n-1 are 2s
        
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo += 1
                mid += 1
        
            elif a[mid] == 1:
                mid += 1
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi -= 1
        


        