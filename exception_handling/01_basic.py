coffe_menu = {"espresso": 1.5, "latte": 2.5, "cappuccino": 3.0}




try:
    order = input("Enter your coffee order (espresso, latte, cappuccino): ").strip().lower()
    price = coffe_menu[order]
    print(f"The price of your {order} is ${price:.2f}")
except KeyError:
    print(f"Sorry, we don't have {order} on the menu.")