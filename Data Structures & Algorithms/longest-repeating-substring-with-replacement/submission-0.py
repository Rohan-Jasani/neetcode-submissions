class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        freq = defaultdict(int)
        max_len = 0
        total_f = 0
        for j in range( n ):
            freq[s[j]] += + 1
            total_f += 1
            while total_f - max(freq.values()) > k:
                freq[s[i]]-=1
                total_f -= 1
                i+=1
            max_len = max( max_len, j-i+1 )
        
        return max_len