class Animal:
    alive = True  # Class variable

    def __init__(self):
        pass

    def eat(self):
        return "This animal is eating."
    
    def sleep(self):
        return "This animal is sleeping."
    

class Rabbit(Animal):
    def run(self):
        return "The rabbit is running."


class Fish(Animal):
    def swim(self):
        return "The fish is swimming."


class Hawk(Animal):
    def fly(self):
        return "The hawk is flying."
    

rabbit = Rabbit()
print(rabbit.run())
print(rabbit.eat())