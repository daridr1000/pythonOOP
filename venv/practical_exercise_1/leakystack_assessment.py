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
        self._index=0 # initialise the index where each element is pushed or popped

    def push(self,number):
        self._storage[self._index]=number # pushes the element in the appropiate place
        self._index+=1 # moves the index to the next position in the array
        if self._index==self._capacity:
            self._index=0 # if the index reaches the end of the array, reinitialising it to 0 as we have to push elements at the beginning of the circular array
        if self._capacity - self._storage.count(None) == self._maxlen + 1:
            # if the stack limit is reached, memorises the element which has to be eliminated
            element_to_forget=self._storage[self._index - self._maxlen - 1]
            self._storage[self._index - self._maxlen - 1] = None # deletes the element
            raise Full("reach stack limit, forget element "+str(element_to_forget) +
                       "\nafter push "+str(number)+" "+str(self._storage)) # raises the appropiate error and the element which was eliminated and displays the array updated with the new pushed element
    def pop(self):
        if not self.is_empty(): # if the stack is not empty ...
            number=self._storage[self._index-1] #memorises the number which has to be popped
            self._storage[self._index-1]=None # deletes the last element which was pushed in the stack
            self._index-=1 # decreases the index to the new empty position in the array where another element would be pushed
            return number # returns the number which was popped
        raise Empty("Stack is empty") # raises an appropiate error if the stack is empty

    def is_empty(self):
        # checks if the stack is empty(contains only "None" elements), returns True if it is and false if it isn't
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



