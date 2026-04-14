class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+1)]
        output = []
        i = 0

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1

        for keys, values in counts.items():
            buckets[values].append(keys)

        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] == []:
                continue
            output.extend(buckets[i])
            if len(output) == k:
                break
            
        return output

        
        