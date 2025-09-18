def serve_coffe(flavour):
    try:
        print(f"Serving your {flavour} coffe...")
        if flavour not in ["espresso", "latte", "cappuccino"]:
            raise ValueError(f"Sorry, we don't have {flavour} on the menu.")
    except ValueError as e:
        print("Error: ",e)
    else:
        print(f"Enjoy your {flavour} coffe!")
    finally:
        print("Next customer please!\n")

serve_coffe("latte")
print("   ")
serve_coffe("mocha")