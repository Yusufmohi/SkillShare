Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python312/SkillShare/Sequence(Stack & Queue)-(QueueviaStack).py
>>> queue=QueueViastack([1])
>>> queue.enqueue(2)
>>> queue.stack
[1, 2]
>>> queue.enqueue(3)
>>> queue.enqueue(4)
>>> queue.stack
[1, 2, 3, 4]
>>> queue.dequeue(2)
1
>>> queue.stack
[2, 3, 4]
>>> queue.dequeue([4])
2
>>> queue.stack
[3, 4]
