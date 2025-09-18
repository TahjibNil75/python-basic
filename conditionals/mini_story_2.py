coffee_order = input("Enter your prefer coffee size:  ").lower().strip()

if coffee_order == "small":
    print(f"Price is 10")
elif coffee_order == "medium":
    print(f"Price is 15")
elif coffee_order == "large":
    print(f"Price is 20")
else:
    print(f"Invalid coffee size: {coffee_order}. Please choose small, medium, or large.")        
