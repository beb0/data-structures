class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        
class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.qsize = 0
    
    def enqueue(self, value):
        if self.start == None:
            self.start = Node(value)
            self.end = self.start
            self.qsize += 1
        else:
            self.new_node = Node(value)
            self.end.next = self.new_node
            self.end = self.new_node
            self.qsize += 1
                   
    def dequeue(self):
        self.temp = self.start.next
        self.start = self.temp
        self.qsize -= 1
    
    def queueSize(self):
        return self.qsize
    