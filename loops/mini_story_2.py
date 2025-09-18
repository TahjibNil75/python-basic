names = ["name1", "name2", "name3", "name4", "name5"]

bills = [1902, 2450,7300, 8900, 1000]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} dollars.")