class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}

        for ch in s:
            counts_s[ch] = counts_s.setdefault(ch, 0) + 1

        for ch in t:
            counts_t[ch] = counts_t.setdefault(ch, 0) + 1

        print(counts_s)
        print(counts_t)

        if counts_s.keys() == counts_t.keys():
            for keys, values in counts_s.items():
                if counts_t[keys] != values:
                    return False
            return True
        else:
            return False