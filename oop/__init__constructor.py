class CoffeOrder:

    def __init__(self, type, size):
        self.type = type
        self.size = size

    def summary(self):
        return f"{self.size}ml {self.type} coffee order placed."
    


orderOne = CoffeOrder("Latte", 250)
print(orderOne.summary())