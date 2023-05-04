#@
class Student:
    def __init__(self , name , age ):
        self.name = name
        self.age = age
    def info(self):

        print(f'Імя: {self.name}, Вік: {self.age}')
student =Student("BAxa",23)
student.info()

#!

class Circle:
    def __init__(self, radius):
        self.radius = radius
# class Animal:

    def area(self):
        return 3.14159 * self.radius ** 2
my_circle = Circle(5)
print(my_circle.area())


##
def sound(self):
        print("Ця тварина виділяє звук")

class Dog( ):
    def sound(self):
        print("auf- gaf gaf ")
my_dog = Dog()
my_dog.sound()
