##### NONLOCAL ######

def update_coffe_order():
    coffe_type = "Latte"  # Local scope
    def change_from_counter():
        nonlocal coffe_type
        coffe_type = "Cappuccino"
    change_from_counter()
    print(f"Change from Counter: Serving {coffe_type} coffee!")

update_coffe_order()