flavours = ["ginger", "Out of Stock", "chocolate", "vanilla", "strawberry", "Discontinued", "mint", "pistachio"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"Available flavour: {flavour}")

print("Thank you for checking our ice cream flavours!")    