class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        n = len(s)
        i = 0
        j = n-1

        def check( s ):
            return s == s[::-1] 
        
        while i < j:
            if s[i]!=s[j]: break
            i+=1
            j-=1
        
        return check( s[:i]+s[i+1:] ) or check( s[:j]+s[j+1:] ) 
