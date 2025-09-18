############### Reduce Code duplication #################

## You are managing busy coffe shop
## You received many orders and want to print each customer's name
## along with the type of coffe the orderd 
#### TASK ######
## - write a function print_order(name, coffee_type)
## - Call it multiple times for different customers


def function(argument):
    pass
function("parameter")


def print_order(name, coffee_type):
    print(f"{name} ordered {coffee_type} coffee!!!")


print_order("customer1", "Latte")
print_order("customer2", "Cappuccino")
print_order("customer3", "Espresso")