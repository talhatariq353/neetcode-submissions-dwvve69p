class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        prefix = 1
        suffix = 1

        l = 0
        r = len(nums) - 1
        while l < len(nums):
            res[l] = prefix
            prefix = nums[l] * prefix
            l += 1
        
        while r >= 0:
            res[r] *= suffix
            suffix = nums[r] * suffix
            r -= 1
        

        return res