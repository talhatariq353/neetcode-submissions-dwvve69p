class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in already_seen:
                return [already_seen[required] ,i]
            else:
                already_seen[num] = i
