#Create an object of class and inherit the composition of one class into another class

class Engine:
    a=10 #static variable
    def __init__(self): #constructor
        self.b=10 #properties
    def m1(self):#Instance method
        print("This is Engine class")
        print("The value of property 'b'=> ",self.b)
        print("The value of static variable in Engine class using 'self'=> ",self.a)
        print("The value of static variable in Engine class using 'class name'=> ",Engine.a)
class Car:
    def __init__(self,CarName,Model,E):#give variable 'E' as a class name Engine
        self.c=30
        self.car=CarName
        self.model=Model
        self.e=E #Using variable of class name inherite all the properties and method
    def m2(self):
        print("Car Name=> ",self.car)
        print("Car Model=> ",self.model)
        self.e.m1()

e1=Engine() #call the Engine class and store all the values in reference variable 'e1'
c=Car("Phantom","Top_Model",e1) #pass all the properties of class Engine using reference variable 'e1'
c.m2()
