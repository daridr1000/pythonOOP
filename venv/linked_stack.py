class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise("Stack is empty")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def print_list(self):
        a = self._head
        for i in range(0, len(self)):
            print(a._element)
            a = a._next

    def delete_duplicates(self):
        for i in range(0,len(self)-1):
            for j in range(1,len(self)):
                a = self.top()
L = LinkedStack()
L.push(200)
L.push(100)
for i in range(0,10):
    L.push(i)
L.print_list()
