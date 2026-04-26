class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        mylist = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1

        for key, value in counts.items():
            mylist[value].append(key)

        for i in reversed(mylist):
            if i == []: continue
            res.extend(i)

            if len(res) >= k:
                break
    
        return res
                

        
        