class Stack:
    def __init__(self):
        self.array = [0] * 100
        self.top = -1

    def IsEmpty(self):
        return self.top == -1
    
    def Push(self, item):
        self.top += 1
        self.array[self.top] = item

    def Pop(self):
        if self.IsEmpty():
            print("Youur array is Empty")
            return None
        else:
            value = self.array[self.top]
            self.top -= 1
            return value
                 
    def peek(self):
        if self.IsEmpty():
            print("Errorrrrrrrrrrr")
        else:
            return self.array[self.top]
        
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.m = 0
        self.s = 0

    def Enqueue(self, item):
        self.s1.Push(item)
        self.m += item

    def Dequeue(self):
        while(not(self.s1.IsEmpty())):
            v = self.s1.Pop()
            self.s2.Push(v)

        self.s = self.s2.Pop()    
        self.m -= self.s

        while(not(self.s2.IsEmpty())):
            r = self.s2.Pop()
            self.s1.Push(r)

    def Display(self):
        print(self.m)



q1 = Queue()
q1.Enqueue(2)
q1.Enqueue(3)
q1.Enqueue(4)
q1.Display()
q1.Dequeue()
q1.Display()
