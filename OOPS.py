class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
E = Employee("Alice", 50000)
M = Manager("Bob", 80000, "Sales")
print(E.name)  # Output: Alice
print(E.salary)  # Output: 50000 

 # EXAMPLE 2
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"   
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!



