class Person:
    def __init__(self, name, age):
        self.name = name            # Public attribute
        self._age = age             # Protected attribute
        self.__salary = 50000       # Private attribute
    
    # Getter for private attribute
    def get_salary(self):
        return self.__salary
    
    # Setter for private attribute
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive.")
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}") 

# Usage
person = Person("Tahir", 19)

# Access public attribute
print(person.name)

# Access protected attribute (not recommended, but possible)
print(person._age)

# Access private attribute (will raise an AttributeError)
# print(person.__salary)

# Access private attribute using getter
print(person.get_salary())

# Modify private attribute using setter
person.set_salary(160000)
person.display_info()
