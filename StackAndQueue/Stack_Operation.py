import sys
class Stack:
    def __init__(self,size_of_stack):
        self.top = -1
        self.size = size_of_stack
        self.list = []
        self.min_element = sys.maxsize
    
    def push(self,input_num):
        if(self.top == self.size - 1):
            print("Overflow Condition")
            return
        else:
            if(self.isEmpty()):
                self.top = self.top + 1
                self.min_element = input_num
                self.list.insert(self.top,input_num)
            else:
                self.top = self.top + 1
                if(input_num < self.min_element):
                    self.min_element = input_num
                    self.list.insert(self.top,2*input_num - self.min_element)
                self.list.insert(self.top,input_num) 
        return

    def pop(self):
        if(self.top < 0):
            print("Underflow Condition")
            return
        else:
            num = self.list[self.top]
            if(num >= self.min_element):
                del self.list[self.top]
            else:
                self.min_element = 2*self.min_element - num
                del self.list[self.top]

            self.top = self.top - 1
            return num
    
    def get_min(self):
        return self.min_element
    
    
    def isEmpty(self):
        if(self.top < 0):
            return True
        return False
    
    
    def isFull(self):
        if(self.top == self.size - 1):
            return True
        return False


if __name__ == "__main__":
    stack = Stack(5)
    for _ in range(5):
        stack.push(int(input("Enter stack element: ")))
    print("Minimum Element: "stack.get_min())
    


