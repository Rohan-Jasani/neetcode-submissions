class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        min_n = min( n1, n2 )
        ans = ''
        for i in range( 0, min_n ):
            ans += word1[i] + word2[i]
        ans += word1[min_n:]
        ans += word2[min_n:]
        return ans