class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = 0
        r = len(nums)-1

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)


        while l < len(nums):
            if l == 0:
                prefix[l] = 1
                suffix[r] = 1
            else:
                prefix[l] = prefix[l-1] * nums[l-1]
                suffix[r] = suffix[r+1] * nums[r+1]
            
            l += 1
            r -= 1
        output = [prefix[i] * suffix[i] for i in range(len(nums))]
        print(prefix)
        print(suffix)
        print(output)
        return output