class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for idx, n in enumerate(nums):
            required = target - n
            if required in already_seen:
                return [already_seen[required], idx]
            if n not in already_seen:
                already_seen[n] = idx