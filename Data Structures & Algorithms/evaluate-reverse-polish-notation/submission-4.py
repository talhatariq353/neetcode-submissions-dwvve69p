class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        val = 0

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            
            elif i == '+':
                val = stack.pop()
                val = val + stack.pop()
                stack.append(val)
            
            elif i == '*':
                val = stack.pop()
                val = val * stack.pop()
                stack.append(val)

            elif i == '-':
                val = stack.pop()
                val = stack.pop() - val
                stack.append(val)
                
            elif i == '/':
                val = stack.pop()
                val = int(stack.pop() / val)
                stack.append(val)
            
            
            print(stack)
        
        return stack[-1]
