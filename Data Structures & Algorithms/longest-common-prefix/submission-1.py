class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_p = 0
        max_p = min( len( s ) for s in strs )
        if max_p == 0: return ''
        while True:
            prefix = strs[0][0:len_p+1]
            for s in strs:
                if s[0:len_p + 1] != prefix: return s[0:len_p ]
            len_p += 1
            if len_p == max_p: break
        return s[0:len_p]

