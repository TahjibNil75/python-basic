## Improving Traceability ####

# Your Shop adds a 10% vat on every order.
# You want this to be consistent and traceable
# Task:
# - write add_vat(price, vat_rate)
# - USe it to compute final prices for 3 orders

def add_vat(price, vat_rate):
    return price + (price * vat_rate / 100)


orders = [100, 270, 390, 569, 200]

for price in orders:
    final_price = add_vat(price, 10)
    print(f"Final price after adding VAT is: {final_price}")