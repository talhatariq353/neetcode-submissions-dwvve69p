class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        strings = set()
        length = 0
        output = 0

        for i, ch in enumerate(s):
            while ch in strings:
                l += 1
                strings.remove(s[l])
            strings.add(ch)
            output = max(output, i-l)
             
        return output
    



        
