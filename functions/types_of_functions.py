def pure_coffe_function(cups):
    return cups * 2


total_cups = 10
def impure_coffe_function(cups):  ## Not recommended
    global total_cups
    total_cups += cups
    return total_cups


coffe_types = ["Espresso", "Latte", "Cappuccino", "Americano", "Latte"]

my_coffe_list = list(filter(lambda coffe: coffe != "Latte", coffe_types))
my_favourite_coffe = list(filter(lambda coffe: coffe == "Latte", coffe_types))

print(my_favourite_coffe)
print(my_coffe_list)