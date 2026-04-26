class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for ch in s:
            counts[ch] = counts.setdefault(ch, 0) + 1

        counts1 = {}
        for ch in t:
            counts1[ch] = counts1.setdefault(ch, 0) + 1

        if counts.keys() == counts1.keys():
            for key, value in counts.items():
                if key not in counts1 or counts1[key] != value:
                    return False
        else:
            return False        
        return True