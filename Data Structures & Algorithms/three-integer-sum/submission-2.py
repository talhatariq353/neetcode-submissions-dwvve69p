class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if num == nums[i-1] and i>0:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                num_sum = num + nums[l] + nums[r]

                if num_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1

                elif num_sum < 0:
                    l += 1
                
                elif num_sum > 0:
                    r -= 1
        
        return res

        
            
            

            

