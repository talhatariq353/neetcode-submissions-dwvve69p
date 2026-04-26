class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)

        l = 0
        r = len(nums) - 1

        while l < len(nums):
            if l == 0:
                left[l] = 1
            else: 
                left[l] = nums[l-1] * left[l-1]
            l += 1

            if r == len(nums) - 1:
                right[r] = 1
            else:
                right[r] = nums[r+1] * right[r+1]
            r -= 1
       
        res = [left[i] * right[i] for i in range(len(nums))]


        return res