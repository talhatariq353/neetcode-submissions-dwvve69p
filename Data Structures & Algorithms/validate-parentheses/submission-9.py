class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []


        for i, ch in enumerate(s):
            if ch in  ('(', '[', '{'):
                stk.append(ch)
            elif ch in (')', ']', '}'):
                if not stk:
                    return False
                elif ( ch == ')' and stk[-1] == '(' ) or (ch == ']' and stk[-1] == '[') or (ch == '}' and stk[-1] == '{'):
                    stk.pop()
                else: return False
        
        if not stk:
            return True
        else:
            return False