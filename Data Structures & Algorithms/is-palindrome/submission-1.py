import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        s = s.lower()
        
        while i < j:
            while i < n and not re.match( r'[a-z0-9]', s[i] ):
                i += 1
            while j >= 0 and not re.match( r'[a-z0-9]', s[j] ):
                j -= 1
            # print( s[i], s[j] )
            if i >= n and j < 0: return True
            if s[i]!=s[j]: return False
            i+=1
            j-=1
        return True