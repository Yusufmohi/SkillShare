class Stack(list):
    def push(self,value):
        self.append(value)
class Queue(list):
    def enqueue(self,value):
        self.append(value)
    def dequeue(self):
        return self.pop(0)

class QueueViastack:
    def __init__(self,iterable):
        self.stack=Stack(iterable)

    def enqueue(self,value):
        self.stack.push(value)

    def dequeue(self,value):
        #Empty Original Stack into new stack
        stack=Stack()
        while len(self.stack):
            stack.push(self.stack.pop())

        value=stack.pop()
        #Empty new stack back into original Stack
        while len(stack):
            self.stack.push(stack.pop())

        return value
