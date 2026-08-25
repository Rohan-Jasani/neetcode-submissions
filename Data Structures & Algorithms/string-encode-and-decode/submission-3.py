class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = '' 
        for word in strs:
            encoded +=  f'{len(word)}#{word}'
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0
        j = 0
        while i < n:
            while s[j]!='#':
                j+=1
            length = int( s[i:j] )
            start = j + 1
            end = j+length
            ans.append( s[start:end+1] )
            i = j + length + 1
            j = i 
        return ans
       
        
