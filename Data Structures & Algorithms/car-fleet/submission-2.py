class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [[position[i],speed[i]] for i in range(len(position))]
        temp.sort(reverse = True)
        stack = []

        print(temp)
        
        for i in temp:
            dist = target - i[0]
            time = dist/i[1]
            
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)