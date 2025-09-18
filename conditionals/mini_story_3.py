device_status = "active"
temperature = 75

if device_status == "active":
    if temperature > 70:
        print("WARNING!!!!Device is active and temperature is above 70 degrees!!!!")
    else:
        print("Device is active and temperature is within safe limits.")    
else:
    print("Device is not active.")