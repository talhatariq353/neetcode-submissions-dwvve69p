class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False

        for ch in s:
            count_s[ch] = count_s.setdefault(ch, 0) + 1
        
        for ch in t:
            count_t[ch] = count_t.setdefault(ch, 0) + 1

        if count_s.keys() == count_t.keys():
            for key, value in count_s.items():
                if count_t[key] != value:
                    return False
        else:
            return False

        return True            

        print(count_s)
        print(count_t)
        