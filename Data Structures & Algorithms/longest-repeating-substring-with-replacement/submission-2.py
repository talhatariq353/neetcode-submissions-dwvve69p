class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        res = 0
        counts = [0] * 26

        for i, ch in enumerate(s):
            counts[ord(ch)-ord('A')] += 1
            while ((i - l + 1) - max(counts)) > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1
                
            res = max(res, i-l+1)

        return res