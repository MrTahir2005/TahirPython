class ParentClass:
    def __init__(self, name):
        self.name = name

    def name1(self):
        print(f"Hello my name is, {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def age1(self):
        print(f"I am {self.age} years old.")

        # Usage
child = ChildClass("Pushpa", 9)
child.name1()
child.age1()



Single Inheritance

class Animal:
    def speak(self):
      print("Iam an animal")

class Dog(Animal):
    def speak(self):
      print("I Bark")

dog = Dog()
dog.speak()


**Multiple Inheritance**

  class A:
  def feature1(self):
    print("I am feature 1")
class B:
  def feature2(self):
    print("I am feature 2")
class C(A,B):
  pass

obj=C()          
obj.feature1()
obj.feature2()







