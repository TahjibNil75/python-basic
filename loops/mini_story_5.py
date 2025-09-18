# For-else

staff = [("employee1", 18), ("employee2", 22), ("employee3", 20), ("employee4", 19)]

for name, age in staff:
    if age >= 20:
        print(f"{name} is eleigible for the manager position.")
        # continue
        # break
else:
    print("No eligible candidates for the manager position.")    