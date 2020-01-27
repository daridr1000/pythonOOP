class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def Animal_detail(self):
        print("Name: ",self.name)
        print("Sound: ", self.sound)
class Dog(Animal):
    def __init__(self,name,sound,family):
        super().__init__(name,sound)
        self.family=family
    def Animal_detail(self):
        super().Animal_detail()
        print("Family: ",self.family)
class Sheep(Animal):
    def __init__(self,name,sound,color):
        super().__init__(name,sound)
        self.color=color
    def Animal_detail(self):
        super().Animal_detail()
        print("Color: ",self.color)