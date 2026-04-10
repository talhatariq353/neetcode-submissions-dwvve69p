class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        answer = [0] * len(nums)

        l = 0
        r = len(nums) - 1

        while l < len(nums):
            if l == 0:
                left[l] = 1
                right[r] = 1
            else:
                left[l] = left[l-1] * nums[l-1]
                right[r] = right[r+1] * nums[r+1]

            l += 1
            r -= 1

        print(left)
        print(right)
        answer = [right[x] * left[x] for x in range(len(nums))]
        
        return answer

#Input = [1,2,3,4]
#left = [1,1,2,6]
#right = [24,12,4,1]