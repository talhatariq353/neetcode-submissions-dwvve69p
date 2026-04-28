class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0
        

        for i, height in enumerate(heights):
            if not stack or height > stack[-1][0]:
                stack.append([height, i])
            elif stack and height < stack[-1][0]:
                for h in reversed(stack):
                    if height < h[0]:
                        h[0] = height
                    else: break
            #print(stack)

            j = 0
            while j < len(stack):
                area = (i - stack[j][1] + 1) * stack[j][0]
                output = max(output, area)
                j += 1
            
        return output
                
