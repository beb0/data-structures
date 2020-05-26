class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        self.new_node = Node(value)
        self.new_node.next = self.head
        self.head = self.new_node
        self.size += 1
                 
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop") 
            self.size = 0
        else:
            print(self.head.value)
            self.head = self.head.next
            self.size -= 1
                               
    def isEmpty(self):
        return self.head == None
    
    def sizeOfStack(self):
        print("Stack Size: " + str(self.size))
    
    def printStack(self):
        while self.head != None:
            print(self.head.value)
            self.head = self.head.next
