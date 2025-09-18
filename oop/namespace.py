class Coffee:
    origin = "Colombia"

print(Coffee.origin)    

Coffee.is_hot = True
print(Coffee.is_hot)

## Creating objects from class

Espresso = Coffee()
Espresso.is_hot = False
print(f"Espresso origin: {Espresso.origin}")
print(f"CLASS:", Coffee.is_hot)
print(f"Espresso is hot: {Espresso.is_hot}")