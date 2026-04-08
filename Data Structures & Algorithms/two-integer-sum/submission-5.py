class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iteration = 0

        n = len(nums)
        diffs = []
        indices = []
        for i in range(n):
            diffs.append(target - nums[i])  
            indices.append(i)
            
        

        for i in diffs:
            if i in nums and nums.index(i) != indices[iteration]:
                return sorted([indices[iteration], nums.index(i)])
                break
            iteration += 1

