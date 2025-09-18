def serve_coffe():
    coffe_type = "Latte"  # Local scope
    print(f"INSIDE FUNCTION: Serving {coffe_type} coffee!")


coffe_type = "Espresso"
serve_coffe()
print(f"OUTSIDE FUNCTION: Serving {coffe_type} coffee!")

print("                   ")

def coffe_counter():
    coffe_type = "Latte"  # Local scope
    def print_coffe(): # Nested function
        coffe_type = "Cappuccino"
        print(f"INSIDE FUNCTION OF COFFE_TYPE: Serving {coffe_type} coffee!")
    print_coffe()    
    print(f"INSIDE OUTER FUNCTION: Serving {coffe_type} coffee!")

coffe_counter()
    
