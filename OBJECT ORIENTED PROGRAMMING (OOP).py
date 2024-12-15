OBJECT ORIENTED PROGRAMMING (OOP)
1.Creating An OBJECT
# EXAMPLE 1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, My Name is {self.name} and I am {self.age} years old.")

person1 = Person("Tahir", 19)
person1.greet()



Constructors and __ int __ Method
# Example
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius *self.radius

circle1 = Circle(5)
print(f"The area of the circle is {circle1.area()}")





