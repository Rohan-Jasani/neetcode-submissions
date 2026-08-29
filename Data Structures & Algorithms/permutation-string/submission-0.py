from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        freq_win = Counter()
        i=0
        n1 = len(s1)
        for j in range(len(s2)):
            freq_win[s2[j]]+=1

            if j-i + 1 > n1:
                freq_win[s2[i]] -= 1
                i+=1
            
            if freq_win == freq: return True
        return False
