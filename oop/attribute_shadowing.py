class Coffe:
    temperature = "hot"
    strenth = "strong"


prepared_coffee = Coffe()
print(prepared_coffee.temperature)

prepared_coffee.temperature = "cold"
print("After Changing ",prepared_coffee.temperature)

print("Direct Look into class: ", Coffe.temperature)

prepared_coffee.cup = "small"
print("After Adding cup size ", prepared_coffee.cup)

# del prepared_coffee.cup ## Output: None



del prepared_coffee.temperature
print("After Deleting ", prepared_coffee.temperature)