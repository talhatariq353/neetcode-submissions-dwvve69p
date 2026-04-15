class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        previous_max_height_l = 0
        previous_max_height_r = 0
        water_l = [0] * len(height)
        water_r = [0] * len(height)
        water = []
        output = 0


        while height[l] == 0:
            l += 1
            if l >=r:
                return 0
        
        while height[r] == 0:
            r -= 1



        previous_max_height_l = height[l]
        previous_max_height_r = height[r]
        l += 1
        r -= 1

        while l < len(height):
            print(l, r)
            if height[l] <= height[l-1]:
                water_l[l] = previous_max_height_l - height[l]
            
            if height[l] > height[l-1]: 
                if height[l] >= previous_max_height_l:
                    previous_max_height_l = height[l]
                else:
                    water_l[l] = previous_max_height_l - height[l]
            l += 1

        while r >= 0:
            if height[r] <= height[r+1]:
                water_r[r] = previous_max_height_r - height[r]
            
            if height[r] > height[r+1]: 
                if height[r] >= previous_max_height_r:
                    previous_max_height_r = height[r]
                else:
                    water_r[r] = previous_max_height_r - height[r]

            r -= 1
        print(water_l)
        print(water_r)

        for i in range(len(height)):
            water.append(min(water_l[i], water_r[i]))

        print(water)

        for i, num in enumerate(water):
            output = num+output    
        
        return output


