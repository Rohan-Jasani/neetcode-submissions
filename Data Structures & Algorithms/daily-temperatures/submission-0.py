class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(101, 0)]
        ans = [0]*len( temperatures )
        for j, t in enumerate( temperatures ):
            if t <= stack[-1][0]: stack.append( (t, j ) )
            else:
                while stack[-1][0] < t:
                    _, i = stack.pop()
                    ans[i] = j - i
                stack.append( ( t, j ) )
        while len( stack ) > 1:
            _,i = stack.pop()
            ans[i] = 0
        return ans
