class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        max_len = 0
        freq = defaultdict(int)
        for j in range(n):
            freq[ s[j] ] += 1
            while freq[s[j]] > 1:
                freq[s[i]]-=1
                i += 1
            max_len = max( max_len, j-i+1 )
        return max_len