class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = min(heights[l], heights[r]) * (r - l)

        while l < r:

            if heights[l] < heights[r]:
                l += 1
                area = min(heights[l], heights[r]) * (r - l)
                res = max(res, area)

            else:
                r -= 1
                area = min(heights[l], heights[r]) * (r - l)
                res = max(res, area)

        return res