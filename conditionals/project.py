speed_limit = 60
actual_speed = int(input("Enter the actual speed of the vehicle:  "))
is_raining = input("Is it raining? (yes/no): ").strip().lower()
repeat_offender = input("Is this a repeat offender? (yes/no): ").strip().lower()


over_speed = actual_speed - speed_limit


# Adjust tolerance for rainy weather
if is_raining:
    over_speed += 5  # Increase tolerance by 5 km/h if it's raining


if over_speed <= 0:
    print("No fine. Safe driving!")
else:
    if over_speed <= 10:
        fine = 0
        message = "Warning: Speeding detected, but no fine."
    elif over_speed <= 20:
        fine = 200 
        message = "Fine: 200. Moderate speeding."
    elif over_speed <= 30:
        fine = 500
        message = "Fine: 500. Significant speeding."
    else:
        fine = 1000
        message = "Fine: 1000. Severe speeding."

    if repeat_offender and fine < 0:
        fine *= 2    
        message += " Repeat offender penalty applied."


    if fine == 0:
        print(message)  
    else:
        print(f"{message} Total fine: {fine}. Please drive safely!")                