#function

# def addition(num1 = 12, num2 = 13):
#     print(num1 + num2)

# addition(11)

#calling value > default parameters


#oop

#abstraction
#encapsulation
#inheritance
#polymorphism


# public Dog(){

# } cpp and java


# class Dog:
#     breed = "unknown"

#     def __init__(self, breed):
#         self.breed = breed
#         print(self)

# dog = Dog("labrador")
# print(dog.breed)

#abstraction

# class Car:

#     brake = False
#     clutch = False
#     acc = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started")

#     def stop(self):
#         self.brake = True
#         self.clutch = False
#         self.acc = False
#         print("Car stopped")

# car = Car()
# car.start()
# car.stop()



#inheritance has three types:
# single inheritance
# multiple inheritance
# multilevel inheritance

class Animal:
    teeth = "large"


class Dog(Animal):
    breed = "unknown"
    def __init__(self, breed):
        self.breed = breed

dog = Dog("Labrador")
print(dog.teeth)

#multiple inheritance
# class A:
# class B:
# class C(A, B):

#multilevel inheritance
# class A:
# class B(A):
# class C(B):

class ComplexNumber:
    real = 0
    img = 0

    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def output(self):
        print(self.real , "i +", self.img, "j")

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return ComplexNumber(real, img)

    
num1 = ComplexNumber(1, 2)

num1.output()
num2 = ComplexNumber(4, 6)

num2.output()

num3 = num1 + num2

num3.output()
