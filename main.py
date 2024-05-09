class Animal:
    ...

class Dog(Animal):
    ...

class Vehicle:
    ...

class BMW(Vehicle):
    ...

if __name__ == "__main__":
    d = Dog()
    a = Animal()
    b = BMW()
    print(isinstance(d, Animal))
    print(isinstance(a, Animal))
    print(isinstance(b, Animal))