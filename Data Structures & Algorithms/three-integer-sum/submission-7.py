class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        
        for i, num in enumerate(nums):
            if num == nums[i-1] and i>0:
                continue
            l = i+1
            r = len(nums) - 1

            while l < r:


                
                if num + nums[l] + nums[r] > 0:
                        r -= 1
                    
                elif num + nums[l] + nums[r] < 0:
                        l += 1

                elif num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    r-=1  
                    while r > l and nums[r] == nums[r+1]:
                        r -=1  


                

               
        return res
            
