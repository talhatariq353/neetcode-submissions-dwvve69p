class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+1)]
        answer = []

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1

        print(counts)
        

        for key, value in counts.items():
            buckets[value].append(key)

        print(buckets)

        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] == []:
                continue
            else:
                answer.extend(buckets[i])
            if len(answer) == k:
                break
        
        return answer


