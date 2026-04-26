class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0

        for i in tokens:
            
            if i == '+':
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

            else:
                stack.append(int(i))
                        
            
            print(stack)
        
        return stack[-1]
