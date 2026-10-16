class MinStack:

    def __init__(self):

        self.min = 0
        self.stack = [] # list of tuples where each integer stores it's predecessor value 

    def push(self, val: int) -> None:
        
        self.stack.append( (val, self.getMin()) ) # Push value with current Minimum

        if len(self.stack) <= 1:
            self.min = val
        else:
            self.min = min(self.min, val) # Update current Minimum

    def pop(self) -> None: 
        top = self.stack[-1]

        if top[0] == self.getMin(): # If we're popping current Minimum
            self.min = top[1] # Set current minimum to current minimum's predecessor

        self.stack.remove(top)

    def top(self) -> int:
        return self.stack[-1][0] # Last list's value

    def getMin(self) -> int:
        return self.min
