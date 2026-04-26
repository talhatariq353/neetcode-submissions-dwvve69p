class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for ch in s:
            count_s[ch] = count_s.setdefault(ch, 0) + 1
        
        for ch in t:
            if ch in count_s and count_s[ch] != 0:
                count_s[ch] -= 1
            else: return False

        return max(count_s.values()) == 0
        