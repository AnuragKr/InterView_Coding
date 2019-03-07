# Node class
class Node:
    #Function to initialize the node object
    def __init__(self,data):
        self.data = data # Assign data
        self.next = None # Initialize

# Linked List class    
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


    def create_node(self):
        input_num = int(input("Enter data element: "))
        if(self.head == None):
            self.head = Node(input_num)
        else:
            q = self.head
            while(q.next != None):
                q = q.next
            q.next = Node(input_num)


    def traverse(self):
        if(self.head is None):
            print("Linked List is empty.")
        else:
            q = self.head
            while(q != None):
                print(q.data)
                q = q.next
        return


    def length(self):
        count = 0
        if(self.head is None):
            return count
        else:
            q = self.head
            while(q != None):
                q = q.next
                count = count + 1
        return count


    def insert_at_begin(self):
        input_num = int(input("Enter data element at begining: "))
        new_node = Node(input_num)
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return


    def insert_at_pos(self,pos):
        length = self.length()
        if((pos <= 0) or (pos > length + 1)):
            print("Invalid Position")
            return
        elif(pos == 1):
            self.insert_at_begin()
        elif(pos == length + 1):
            self.create_node()
        else:
            count = 1
            input_num = int(input("Enter data element for a position:"))
            new_node = Node(input_num)
            q = self.head
            while(count < pos - 1):
                q = q.next
                count = count + 1
            new_node.next = q.next
            q.next = new_node


    def middle_element(self):
        slow = self.head
        fast = self.head
        while((fast != None) and (fast.next != None) and (fast.next.next != None)):
            slow = slow.next
            fast = fast.next.next
        return slow.data


    def find_cycle(self):
        slow = self.head
        fast = self.head
        while((fast != None) and (fast.next != None) and (fast.next.next != None)):
            if(slow == fast):
                print("Cycle Exist.")
                return
            slow = slow.next
            fast = fast.next.next
        print("Cycle does not exist.")
        return


    def delete_at_begin(self):
        if(self.head is None):
            print("Linked List is empty.")
        elif(self.head.next is None):
            self.head = None
        else:
            self.head = self.head.next
        return
    

    def delete_at_end(self):
        if(self.head is None):
            print("List is empty.")
        elif(self.head.next is None):
            self.head = None
        else:
            p = None
            q = self.head
            while(q.next != None):
                p = q
                q = q.next
            p.next = None

    
    def delete_at_pos(self,pos):
        length = self.length()
        if((pos <= 0) or (pos > length + 1)):
            print("Invalid Position")
            return
        elif(pos == 1):
            self.delete_at_begin()
        elif(pos == length + 1):
            self.delete_at_end()
        else:
            count = 1
            p = None
            q = self.head
            while(count < pos):
                p = q
                q = q.next
                count = count + 1
            p.next = q.next
            q.next = None


    def reverse(self):
        p = None
        q = None
        r = self.head
        while(r):
            q = r.next
            r.next = p
            p = r
            r = q
        self.head = p
    
    
    def rotate_anti_clockwise(self,k = 4):
        if(k == 0):
            return
        current = self.head
        count = 1

        while(count < k and current is not None):
            current = current.next
            count += 1

        if(current is None):
            return

        kthNode = current

        while(current.next is not None):
            current = current.next
        
        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None
        
        return

        
if __name__ == '__main__':
    linked_list = LinkedList()
    for _ in range(6):
        linked_list.create_node()
    # linked_list.insert_at_begin()
    # linked_list.insert_at_pos(4)
    # print("Middle Element " + str(linked_list.middle_element()))
    # linked_list.delete_at_begin()
    # print("Listing Element after first deletion. ")
    # linked_list.traverse()
    # linked_list.delete_at_end()
    # print("Listing Element after second deletion. ")
    # linked_list.traverse()
    # linked_list.delete_at_pos(2)
    # print("Listing Element after deleting from given position.")
    # linked_list.traverse()
    # linked_list.reverse()
    # print("Reversing Linked List.")
    # linked_list.traverse()
    print("Rotating a Linked List Anti-Clockwise")
    linked_list.rotate_anti_clockwise(3)
    linked_list.traverse()
    
