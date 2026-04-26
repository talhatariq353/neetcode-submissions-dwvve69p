class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        my_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            my_dict[tuple(count)].append(s)

        for key, value in my_dict.items():
            res.append(value)
        
        return res



