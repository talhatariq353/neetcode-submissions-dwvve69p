class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        open = ['(', '[', '{']
        close = [')', ']', '}']

        for i, ch in enumerate(s):
            if ch in open:
                stk.append(ch)
            elif ch in close:
                if not stk:
                    return False
                elif ( ch == ')' and stk[-1] == '(' ) or (ch == ']' and stk[-1] == '[') or (ch == '}' and stk[-1] == '{'):
                    stk.pop()
                else: return False
        
        if not stk:
            return True
        else:
            return False