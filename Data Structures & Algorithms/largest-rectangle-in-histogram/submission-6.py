class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0
        index = 0

        for i, height in enumerate(heights):
            if not stack or height >= stack[-1][0]:
                stack.append([height, i])
                area = stack[-1][0] * 1
                output = max(area, output)

            else:
                while stack and height < stack[-1][0]:
                    index = stack[-1][1]
                    stack.pop()     
                stack.append([height, index])
            #print(stack)

            j = 0
            while j < len(stack):
                area = (i - stack[j][1] + 1) * stack[j][0]
                output = max(output, area)
                j += 1
            
        return output

        
                
