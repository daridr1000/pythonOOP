#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Assessment 1:  10% of your overall mark for the course
#


from array_stack import ArrayStack
import unittest


class Full(Exception):
    pass


class Empty(Exception):
    pass


class MyLeakyStack(ArrayStack):
    """complete this class by adding more functions within the class"""
    def __init__(self, maxlen, capacity):
        """note: this function is partially completed"""
        super().__init__()
        self._maxlen = maxlen
        self._capacity = capacity  # size of the circular array
        self._storage = [None] * capacity  # initialise storage room, this is treated as a circular array
        self._index=0
        self._element_to_forget=None

    def push(self,number):
        self._storage[self._index]=number
        self._index+=1
        if self._index==self._capacity:
            self._index=0
        if self._capacity - self._storage.count(None) == self._maxlen + 1:
            self._element_to_forget=self._storage[self._index - self._maxlen - 1]
            self._storage[self._index - self._maxlen - 1] = None
            raise Full("reach stack limit, forget element "+str(self._element_to_forget) +
                       "\nafter push "+str(number)+" "+str(self._storage))

    def pop(self):
        if not self.is_empty():
            number=self._storage[self._index-1]
            self._storage[self._index-1]=None
            self._index-=1
            return number
        raise Empty("Stack is empty")

    def is_empty(self):
        if self._capacity==self._storage.count(None):
            return True
        return False


if __name__ == '__main__':

    S = MyLeakyStack(5, 10)   # stack size should be 5 and the capacity of the array should be 10
    for i in range(12):
        try:
            S.push(i)
            print("after push "+str(i), S._storage)
        except Exception as e:
            print(e)
    for i in range(6):
        try:
            a=S.pop()
            print("after pop "+str(a), S._storage)
        except Exception as e:
            print(e, S._storage)

    for i in range(5):
        try:
            S.push(i+100)
            print("after push " + str(i+100), S._storage)
        except Exception as e:
            print(e, S._storage)



