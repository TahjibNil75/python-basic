def make_coffe(beans, milk, sugar):
    print(f"Making coffee with {beans} beans, {milk} milk, and {sugar} sugar.")

make_coffe("Arabica", "whole milk", "2 teaspoons") #positional arguments
make_coffe(beans="Robusta",sugar="1 teaspoon", milk="skim milk") #keyword arguments



print("        *args & **kwargs         ")

####### args (arguments) ######
####### *args (key valuearguments) ######

def make_specail_coffee(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

make_specail_coffee("black coffee", "sugar", "milk", cream="whipped", flavor="vanilla")



print("    Default trap     ")
def coffe_order(order=[]):
    order.append("latte")
    print("Your coffee order:", order)

coffe_order() # This will show the order list with "latte" added to it.
coffe_order()  # This will show the same order list as before, demonstrating the mutable default argument trap.   
coffe_order(["espresso"])  # This will create a new order list with "latte" added to it.


print("    avoid Default trap      ")

def coffe_order_fixed(order=None):
    if order is None:
        order = []
    print("Your coffee order:", order)

coffe_order_fixed()  # This will show an empty order list.
coffe_order_fixed()  # This will show an empty order list again, avoiding the mutable default argument trap.
coffe_order_fixed(["espresso"])  # This will create a new order list with "espresso" added to it.
