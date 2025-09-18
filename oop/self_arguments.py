class Coffe:
    size = 150

    def describe(self):
        return f"This coffee is {self.size}ml."
    

cup = Coffe()
print(cup.describe())
print(Coffe.describe(cup))


cup_two = Coffe()
cup_two.size = 200
print(Coffe.describe(cup_two))