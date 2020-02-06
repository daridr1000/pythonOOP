import random
class Polynom:
    MAXIMAL=7
    def __init__(self,grade):
        self.grade=grade+1
        self.coefficients=[None]*self.grade
        self.polynomialform=""
    def set_coefficients(self):
        for i in range(0,self.grade):
            self.coefficients[i]=random.randint(0,Polynom.MAXIMAL)
    def get_polynom(self):
        self.polynomialform=str(self.coefficients[0])
        for i in range(1,len(self.coefficients)):
                if self.coefficients[i]!=0:
                    if self.coefficients[i]==1:
                        self.polynomialform+="+X^{}".format(i)
                    else:
                        self.polynomialform += "+{}X^{}".format(self.coefficients[i], i)
    def differentiate(self):
        for i in range(0,len(self.coefficients)):
            self.coefficients[i]=self.coefficients[i]*i
        self.coefficients.pop(0)


polynom=Polynom(4)
polynom.set_coefficients()
polynom.get_polynom()
print(polynom.coefficients)
print(polynom.polynomialform)
polynom.differentiate()
print(polynom.coefficients)
polynom.get_polynom()
print(polynom.polynomialform)
polynom.differentiate()
print(polynom.coefficients)
polynom.get_polynom()
print(polynom.polynomialform)
polynom.differentiate()
print(polynom.coefficients)
polynom.get_polynom()
print(polynom.polynomialform)
polynom.differentiate()
print(polynom.coefficients)
polynom.get_polynom()
print(polynom.polynomialform)
