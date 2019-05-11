class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []
    
    def push(self,val):
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val,self.maxes[-1]))
        else:
            self.maxes.append(val)
    
    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

if __name__ == "__main__":
    maxStack = MaxStack()
    for _ in range(5):
        maxStack.push(input("Enter Element:"))
    print(maxStack.maxes,maxStack.stack)  
    maxStack.pop()
    maxStack.pop() 
    print(maxStack.max())