class ArrStack:
    def __init__(self):
        self.stack = [None] * 1
        self.head = -1
        
    def push(self, item):
        if self.head + 1 == len(self.stack):
            self.resize(len(self.stack)*2)
        
        self.head += 1
        self.stack[self.head] = item
                       
    def pop(self): 
        if self.head == int((len(self.stack) / 4)):
            self.resize(len(self.stack)/2)
            
        self.stack[self.head] = None
        self.head -= 1
    
    def resize(self, length):
        self.arr = [None] * int(length)
        
        for i in range(self.head+1):
            self.arr[i] = self.stack[i]

        self.stack = self.arr

    def printStack(self):
        print(self.stack)
        