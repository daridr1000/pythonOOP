class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def add_first(self,e):
        newest = _Node(e)
        newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self,e):
        newest = _Node(e)
        if self._head is None:
            self._head = newest
            return
        laste = self._head
        while(laste._next):
            laste = laste._next
        laste._next = newest
        self._size += 1

    def remove_node(self,removed_element):
        self._size -= 1
        head = self._head
        if self._head is not None:
            if self._head._element == removed_element:
                self._head = head._next
                head = None
                return
        while head is not None:
            if head._element == removed_element:
                break
            prev = head
            head = head._next
        if self._head == None:
            return
        prev._next = head._next
        head = None

    def remove_middle_node(self,removed_element):
        node = _Node

    def remove_duplicates(self):
        head = self._head
        while head is not None:
            next_head = head._next
            while next_head is not None:
                if next_head is None:
                    break
                if head._element == next_head._element:
                    self.remove_node(head._element)
                next_head = next_head._next
            head = head._next

    def kth_to_last(self,k):
        l=0
        head = self._head
        while head is not None:
            element = head._element
            if l == self._size - k:
                return element
            l += 1
            head = head._next

    def print_list(self):
        val = self._head
        while val is not None:
            print(val._element)
            val = val._next

L = LinkedList()
for i in range(0,10):
    L.add_first(i)
    L.add_last(5)
for i in range(0,10):
    L.add_first(i)
L.print_list()
L.remove_duplicates()
print("New list:")
L.print_list()
print("Number of nodes",L._size)
print("Element is:",L.kth_to_last(4))