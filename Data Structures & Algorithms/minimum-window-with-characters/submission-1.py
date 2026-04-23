class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}
        
        have = 0
        res = [-1, -1]
        resLen = float("infinity")

        for i, ch in enumerate(t):
            countT[ch] = countT.setdefault(ch, 0) + 1

        need = len(countT)
        print(countT)


        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.setdefault(ch, 0) + 1
            
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l = res[0]
        r = res[1]

        print(resLen)

        if resLen == float('infinity'):
            return ""
        else:
            return s[l: r+1] 


                
            


