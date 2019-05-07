# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize

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

    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)

    def get_head(self):
        return self.head

    def insert_at_begin(self):
        input_num = int(input("Enter data element at begining: "))
        new_node = Node(input_num)
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return

    def insert_at_pos(self, pos):
        length = self.length(self.get_head())
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

    def delete_at_pos(self, pos):
        length = self.length(self.get_head())
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
        current, prev = self.head, None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def rotate_anti_clockwise(self, k=4):
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

    # Finding intersection of two linked list
    def intersection(self, a, b):
        m, n = self.length(a), self.length(b)
        cur_a, cur_b = a, b

        if m > n:
            for _ in range(m-n):
                cur_a = cur_a.next
        else:
            for _ in range(n-m):
                cur_b = cur_b.next

        while cur_a.data != cur_b.data:
            cur_a = cur_a.next
            cur_b = cur_b.next
        print(cur_a.data)

    # Rearrange a linked list to alternate high-low
    def alternate(self, head):
        prev = head
        cur = head.next
        while cur:
            if prev.data > cur.data:
                prev.data, cur.data = cur.data, prev.data
            if not cur.next:
                break
            if cur.next.data > cur.data:
                cur.next.data, cur.data = cur.data, cur.next.data

            prev = cur.next
            cur = cur.next.next

    #Add two linked lists that represent numbers
    def add(self,node0_head,node1_head,carry = 0):
        new_head = None
        sum_list = []
        while(node0_head and node1_head):
            node0_val = node0_head.data if node0_head else 0
            node1_val = node1_head.data if node1_head else 0
            total = node0_val + node1_val + carry
            sum_list.append(total%10)
            
            node0_head = node0_head.next if node0_head else None
            node1_head = node1_head.next if node1_head else None
            carry = 1 if total >= 10 else 0
            if(node0_head is None and node1_head is None and carry > 0):
                sum_list.append(carry)
        
        for num in sum_list:
            if(new_head == None):
                new_head = Node(num)
            else:
                q = new_head
                while(q.next != None):
                    q = q.next
                q.next = Node(num)
        
        print("Summation: ")
        while(new_head):
            print(new_head.data)
            new_head = new_head.next

if __name__ == '__main__':
    linked_list = LinkedList()
    second_linked_list = LinkedList()

    print("Enter First Linked List Item:")
    for _ in range(2):
        linked_list.create_node()

    print("Enter Second Linked List Item:")
    for _ in range(2):
        second_linked_list.create_node()

    #print("Length:" + str(linked_list.length(linked_list.get_head())))
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
    #print("Reversing Linked List.")
    # linked_list.traverse()
    #print("Rotating a Linked List Anti-Clockwise")
    # linked_list.rotate_anti_clockwise(3)
    # linked_list.traverse()
    # linked_list.intersection(linked_list.get_head(),second_linked_list.get_head())
    #linked_list.alternate(linked_list.get_head())
    #print("Rearranging Linked List from low to high.")
    #linked_list.traverse()
    linked_list.add(linked_list.get_head(),second_linked_list.get_head())
