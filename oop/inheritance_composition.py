class BaseCoffe:
    def __init__(self, type):
        self.type = type

    def prepare(self):
        return f"Preparing {self.type} coffee."
    

class LatteCoffe(BaseCoffe):
    def add_milk(self):
        return f"Adding milk to {self.type} coffee."

class CoffeShop:
    coffee_class = BaseCoffe

    def __init__(self):
        self.coffe = self.coffee_class("Generic")

    def serve_coffee(self):
        print(f"Serving {self.coffe.type} coffee in the shop.") 
        self.coffe.prepare()

class fancyCoffeShop(CoffeShop):
    coffe_cls = LatteCoffe        


shop = CoffeShop()
shop.serve_coffee()
shop.coffe = LatteCoffe("Latte")
fancyCoffeShop.coffe_cls.add_milk()