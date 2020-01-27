class Student:
    def __init__(self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio
    def __totalObtained(self):
        return(self.phy+self.bio+self.chem)
    def Percentage(self):
        return(Student.__total(self)/3)



student=Student("Darius",80,70,97)
print(student.percentage())