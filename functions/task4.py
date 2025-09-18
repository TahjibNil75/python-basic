### Improving Readability #####
## Instaed of writting formulas everywhere, create a function
## Task ##
# write calculate_bill(cups, price_per_cup)
# Retunr total bill
# Use this function for multiple orders

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 5)
print(my_bill)
print(f"My total bill is: ", calculate_bill(2, 50))