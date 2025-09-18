def favourite_coffe_shop():
    pass

print(favourite_coffe_shop())

def sold_cups():
    return 100

total = sold_cups()
print(f"Total cups sold: {total}")



## EARLY RETURN #####

def coffe_status(cups_left):
    if cups_left > 0:
        return "Coffe is available!"
    else:
        return "Coffe is sold out!"
    print("This line will never be executed.")
    
print(coffe_status(0))
print(coffe_status(10))


## Multiple Returns #####
def coffe_sale_report():
    return 100, 20, 5 # total_cups, sold_cups, cups_left

total_cups, sold_cups, cups_left = coffe_sale_report()
print(f"Total cups: {total_cups}, Sold cups: {sold_cups}, Cups left: {cups_left}")