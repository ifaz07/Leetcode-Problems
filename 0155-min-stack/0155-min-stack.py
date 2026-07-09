class MinStack(object):

    def __init__(self):
        self.min = 2147483650
        self.stack = []

    def push(self, val):

        if len(self.stack) == 0:
            self.min = val
            self.stack.append(val)
            return

        if val < self.min:
            self.stack.append(2*val - self.min)
            self.min = val
        else:
            self.stack.append(val)
        

    def pop(self):

        if len(self.stack) == 0:
            return None

        if self.stack[-1] < self.min:
            self.min = 2*self.min - self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()
    
    def top(self):

        if self.stack[-1] < self.min:
            return self.min
        else:
            return self.stack[-1]
        

    def getMin(self):
        return self.min
