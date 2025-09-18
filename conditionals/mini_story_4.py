# ternay operator 


order_amount = int(input("Enter the order amount: "))

delivary_fee = 0 if order_amount >= 200 else 20


print(f"Delivery fee is: {delivary_fee}")