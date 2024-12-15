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

s1 = Stack()
s1.Push(2)
s1.Push(3)
s1.Push(22)
print("last item is:", s1.peek())
s1.Pop()
print("last item is:", s1.peek())
  

