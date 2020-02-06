import math
import random
class Radius(Exception):
    pass

class Point:
    def __init__(self,x=float,y=float,**kwargs):
        super().__init__(**kwargs)
        self.__X=x
        self.__Y=y
    def __verify_points(self,point):
        if not (isinstance(point, float)):
            raise Radius("Points should be both float numbers!")
    def get_xcoord(self):
        self.__verify_points(self.__X)
        return self.__X
    def get_ycoord(self):
        self.__verify_points(self.__Y)
        return self.__Y
    def distance_from_origin(self):
        self.__verify_points(self.__X)
        self.__verify_points(self.__Y)
        return math.sqrt(self.__X**2+self.__Y**2)
    def __str__(self):
        self.__verify_points(self.__X)
        self.__verify_points(self.__Y)
        return("Point :" + str(self.__X)+" "+str(self.__Y) +" " + str(self.distance_from_origin()))
class Shape:
    def __init__(self,col='',centre=Point(random.random(),random.random()),**kwargs):
        super().__init__(**kwargs)
        self.__colour=col
        self.__centre=[centre.get_xcoord(),centre.get_ycoord()]
    def get_colour(self):
        return self.__colour
    def get_centre(self):
        return self.__centre
class Circle(Shape):
    def __init__(self,rad=None,**kwargs):
        super().__init__(**kwargs)
        self.__radius=rad
    def __verify_radius(self):
        if not (isinstance(self.__radius, float)):
            raise Radius("Radius should be a float number!")
        else:
            if self.__radius < 0:
                raise Radius("Radius should be positive!")
    def get_radius(self):
        self.__verify_radius()
        return self.__radius
    def get_area(self):
        self.__verify_radius()
        return math.pi*(self.__radius**2)
    def __str__(self):
        return("Circle : "+ str(self.__radius)+ " " + self.get_colour()+ " " +str(self.get_area())
               +" ("+str(self.get_centre()[0]) +"," + str(self.get_centre()[1])) +")"
class Cylinder:
    def __init__(self,hei,rad):
        self.__height=hei
        self.__radius=Circle(rad).get_radius()
    def __verify_height(self):
        if not (isinstance(self.__height, float)):
            raise Radius("Height should be a float number!")
        else:
            if self.__radius < 0:
                raise Radius("Heigth should be positive!")
    def get_area(self):
        self.__verify_height()
        return(2*math.pi*(self.__radius)*self.__height*(self.__radius+self.__height))
    def get_volume(self):
        self.__verify_height()
        return(math.pi*(self.__radius**2)*self.__height)
    def __str__(self):
        return("Cylinder:" + str(self.__height)+" " + str(self.__radius)+ " " +
               str(self.get_area())+" "+str(self.get_volume()))
class Rectangle(Shape):
    def __init__(self,wid=None,len=None,**kwargs):
        super().__init__(**kwargs)
        self.__width=wid
        self.__length=len
    def __verify_sides(self):
        if not (isinstance(self.__width, float) and isinstance(self.__length, float)):
            raise Radius("Length and width should be both float numbers!")
        else:
            if self.__width < 0 or self.__length<0:
                raise Radius("Radius should be positive!")
    def get_area(self):
        self.__verify_sides()
        return self.__width*self.__length
    def get_perimeter(self):
        self.__verify_sides()
        return 2*(self.__width)*(self.__length)
    def __str__(self):
        return("Rectangle : "+ str(self.__width)+ " "+str(self.__length)+" " + self.get_colour()+ " "
               +str(self.get_area()) + " " + str(self.get_perimeter())
        +" ("+str(self.get_centre()[0]) +"," + str(self.get_centre()[1]) +")" )


def test_shapes():
    shape=Shape("red")
    print(shape.get_colour())
    circle=Circle()
    circle1=Circle(col="red",rad=1.23)
    print(circle1)
    print(circle1.get_colour())
    print(circle1.get_radius())
    print(circle1.get_area())

    circle2= Circle(col="blue", rad=math.sqrt(1/math.pi))
    print(circle2)
    print(circle2.get_colour())
    print(circle2.get_radius())
    print(circle2.get_area())

    rectangle=Rectangle(col="orange",len=10.0,wid=2.0)
    print(rectangle)

    point=Point(4.0,3.0)
    print(point)
    circle1222=Circle(rad=2.5)
    print(circle1222)

    print(Circle(3.0).get_radius())
    cyl=Cylinder(2.0,3.0)
    print(cyl)
test_shapes()