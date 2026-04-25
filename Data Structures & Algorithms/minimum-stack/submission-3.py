class MinStack:

    def __init__(self):
        self.stack = []
        self.track = []
        self.minimum = float('infinity')

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append(val)
            self.minimum = val
            self.track.append(self.minimum)
        else:
            self.stack.append(val)
            
            if val <= self.minimum:
                self.minimum = val
                self.track.append(self.minimum)

    def pop(self) -> None:
        if self.stack[-1] == self.minimum:
            self.track.pop()
            if self.track:
                self.minimum = self.track[-1]
            else: 
                self.minimum = float('infinity')
        self.stack.pop()

        
    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minimum
        
