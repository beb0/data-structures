class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        self.node = Node(data)
        self.node.next = self.head
        self.head = self.node

    def insertAtEnd(self, data):   
        if self.head == None:
            self.insertAtStart(data)
        else:    
            while self.node.next != None:
                self.node = self.node.next     
            self.node.next = Node(data)

    def insertAtIndex(self, index, data):
        if index > self.listCount() or index < 0:
            print("index not found")
        elif index == 0:
            self.insertAtStart(data)
        elif index == self.listCount():
            self.insertAtEnd(data)       
        else:     
            self.temp = self.head
            self.temp1 = self.head
            self.count = 0 

            while self.count != index:
                self.temp1 = self.temp
                self.temp = self.temp.next
                self.count += 1

            self.new_node = Node(data)
            self.new_node.next = self.temp
            self.temp1.next = self.new_node
            
    def deleteAtIndex(self, index):
        if (self.isEmpty()):
            print("list is empty")
        elif index == None:
            pass
        elif index > self.listCount() or index < 0:
            print("there's no such an index " + str(index))      
        elif index == 0:
            self.head = self.head.next            
        elif index == self.listCount():
            self.temp = self.head
            self.count = 0         
            while self.count != index:
                self.temp1 = self.temp
                self.temp = self.temp.next
                self.count += 1
            self.temp1.next = None            
        else:
            self.temp = self.head
            self.count = 0 
            while self.count != index:
                self.temp1 = self.temp
                self.temp = self.temp.next
                self.count += 1
            self.temp1.next = self.temp.next
            
    def getValueByIndex(self, value):
        self.index = 0 
        self.temp = self.head               
        while self.temp.data != value:
            self.temp = self.temp.next
            self.index += 1
            if self.temp.next == None and self.temp.data != value:
                print (str(value) + " not found")
                self.index = None
                return self.index
        return self.index
            
    def deleteAtValue(self, value):
        self.deleteAtIndex(self.getValueByIndex(value))
    
    def traverse(self):
        self.temp = self.head
        if (self.isEmpty()):
            print("list is empty")
        else:
            while self.temp != None: 
                print(self.temp.data)            
                self.temp = self.temp.next       

    def listCount(self):
        self.temp = self.head
        self.count = 0
        while self.temp.next != None:
            self.temp = self.temp.next
            self.count += 1
        return self.count
    
    def printCount(self):
        if (self.isEmpty()):
            print("list is empty")
        else:
            print("List Count: " + str(self.listCount() + 1))
    
    def isEmpty(self):
        return self.head == None