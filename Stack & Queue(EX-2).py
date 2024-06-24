class Stack(list):
    def push(self,value):
        self.append(value)
class Queue(list):
    def enqueue(self,value):
        self.append(value)
    def dequeue(self):
        return self.pop(0)

queue=Queue([''])
r=int(input())
while len(queue):
    word=queue.dequeue()
    if len(word)==r:
        print(word)
    if len(word)<r:
        queue.enqueue(word+'a')
        queue.enqueue(word+'b')
