class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = min(heights[l], heights[r]) * (r - l)

        while l < r:
            
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            water = min(heights[l], heights[r]) * (r - l)

            if water > max_water:
                max_water = water


        return max_water