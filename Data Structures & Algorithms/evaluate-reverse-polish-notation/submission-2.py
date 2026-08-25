class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'*','-','+','/'}
        n = len( tokens )
        stack = []
        for token in tokens:
            # print( stack )
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '*': stack.append( val1*val2 )
                elif token == '+': stack.append( val1 + val2 )
                elif token == '-': stack.append( val1 - val2 )
                elif token == '/': stack.append( int( val1 / val2 ) )
            else:
                stack.append( int( token ) )
        return stack.pop()


