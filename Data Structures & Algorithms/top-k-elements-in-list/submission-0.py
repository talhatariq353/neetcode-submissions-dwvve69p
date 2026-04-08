class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [ [] for i in range(len(nums)+1)]
        answer = []
        for i in nums:
            counts[i] = counts.setdefault(i,0) + 1

        for num, count in counts.items():
            buckets[count].append(num)

        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] == []:
                continue
            else:
                answer.extend(buckets[i])
            
            
            if len(answer) == k:
                break

        return answer