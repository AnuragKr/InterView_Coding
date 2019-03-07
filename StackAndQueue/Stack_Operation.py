class Stack:
    def __init__(self,size_of_stack):
        self.top = -1
        self.size = size_of_stack
        self.list = []
    
    def push(self,element):
        if(self.top == self.size - 1):
            print("Overflow Consition")
            return
        else:
            self.top = self.top + 1
            self.list.insert(self.top,element) 

    def pop(self):
        if(self.top < 0):
            print("Underflow Condition")
            return
        else:
            num = self.list[self.top]
            self.top = self.top - 1
            return num

if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Pop: " + str(stack.pop()))


