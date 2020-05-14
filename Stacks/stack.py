class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.first_node = self.head
            self.size += 1
        else:
            self.node = Node(value)
            self.head.next = self.node          
            self.head = self.node
            self.size += 1
            
        
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop stack is empty")
        else:    
            self.iterator = self.first_node
            while self.iterator.next != None:
                self.to_pop = self.iterator
                self.iterator = self.iterator.next
                
            if self.iterator == self.first_node:
                self.head = None
                self.size -= 1
            else:
                self.head = self.to_pop
                self.head.next = None   
                self.size -= 1 
                               
    def isEmpty(self):
        return self.head == None
    
    def sizeOfStack(self):
        print("Stack Size: " + str(self.size))
    
    def printStack(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self.iterator = self.first_node
            while self.iterator != None:
                print(self.iterator.value)
                self.iterator = self.iterator.next
        
