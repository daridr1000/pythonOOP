class ArrayDeque():
    CAPACITY = 20
    def __init__(self):
        self.array=[None]*ArrayDeque.CAPACITY
        self._size=0
        self._first=0
        self._last=-1
    def __len__(self):
        return self._size
    def add_first(self,e):
        self.array[self._first]=e
    def add_last(self,e):
        self.array[self._last]=e
    def first(self):
        return self.array[0]
    def last(self):
        return self.array[-1]
deque=ArrayDeque()
deque.add_first(2)
deque.add_first(4)
print(deque.array)
