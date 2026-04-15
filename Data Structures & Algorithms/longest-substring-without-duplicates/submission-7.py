class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        r = 0
        string = set()
        length = 0
        
        for i, ch in enumerate(s):
            while ch in string:
                l+=1
                string.remove(s[l])
            string.add(ch)
            length = max(length, len(string))
            
        return length