class Rectangle:
    def __init__(self,length,width):
        self.__width=width
        self.__length=length
    def area(self):
        return(self.__length*self.__width)
    def perimeter(self):
        return(2*(self.__length+self.__width))
