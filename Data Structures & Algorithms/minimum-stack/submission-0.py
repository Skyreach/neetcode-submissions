class MinStack:
    # the hint is important, it indicates we should have a separate container to track the min
    # note this works because Python's array is dynamic by default
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    # append is normal, warning: guard against empty minStack
    def push(self, val: int) -> None:
        self.stack.append(val)
        if bool(self.minStack):
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        
    # pop from both
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    # peek from array
    def top(self) -> int:
        return self.stack[-1]
        
    # peek from minStack
    def getMin(self) -> int:
        return self.minStack[-1]

        
