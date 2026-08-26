class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append( val2 )
                stack.append( val1 )
                stack.append( val1 + val2 )
            elif op =='D':
                val1 = stack.pop()
                stack.append( val1 )
                stack.append( 2*val1 )
            elif op == 'C':
                stack.pop()
            else:
                stack.append( int( op ) ) 
            
        return sum(stack)
            