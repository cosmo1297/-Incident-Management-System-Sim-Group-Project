from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()
    def peek(self):
        if self.is_empty():
            return  None;
        return self.items[0]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def __str__(self):
        return f"Queue: {list(self.items)}"
#
# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print("Queue after 3 enqueue operations", q)
# print("Queue size after 3 enqueue operations", q.size())
# print("Dequeue operation", q.dequeue())
# print("Queue size after 1 dequeue operation",q)
# print("Peek",q.peek())