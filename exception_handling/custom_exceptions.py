class OutOfIngredientsError(Exception):
    pass

def make_coffe(milk, sugar):
    if milk < 0 or sugar < 0:
        raise OutOfIngredientsError("Milk and sugar quantities must be non-negative.")
    print("Coffe is ready")


make_coffe(1,-1)