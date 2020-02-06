class Empty(Exception):
  pass

class ArrayQueue:
    def __init__(self):
        self._array=[]
    def __len__(self):
        return len(self._array)
    def is_empty(self):
        return len(self._array)==0
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._array[0]
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        element=self.first()
        self._array.pop(0)
        return element
    def enqueue(self,element):
        self._array+=[element]
queue=ArrayQueue()
queue.enqueue(5)
queue.dequeue()
queue.dequeue()