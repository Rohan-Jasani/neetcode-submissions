class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_ = { '{', '(', '[' }
        map_ = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
        }
        for ch in s:
            if ch in open_: stack.append( ch )
            else:
                if len( stack ) == 0: return False
                ch_open = stack.pop()
                if ch_open != map_[ch]: return False
        return len( stack ) == 0

