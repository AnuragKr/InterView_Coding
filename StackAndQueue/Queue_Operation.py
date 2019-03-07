class Queue:
    def __init__(self,size_of_queue):
        self.front = -1
        self.rear = -1
        self.size = size_of_queue
        self.list = []

    def enqueue(self,element):
        if(self.rear == -1):
            self.front = self.front + 1
            self.rear = self.rear + 1
        else:
            self.rear = self.rear + 1
        self.list.insert(self.rear,element)
    
    def dequeue(self):
        if(self.front == -1):
            print("Underflow Condition")
            return
        num = self.list[self.front]
        if(self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = self.front + 1
        return num

if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeued: " + str(queue.dequeue()))
