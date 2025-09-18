"""
Smart Home Device Tracker
You’re building a Smart Home Device Tracker to monitor the status of electronic devices.

Your Tasks:

Create a class called SmartDevice.

Add a class attribute brand = "HomeTech" (default manufacturer).

In the constructor, accept:

device_name: Name of the smart device.
power_status: True (ON) or False (OFF).

Shadow the class attribute brand by assigning self.brand = "CustomBrand" (to simulate user modification).

Define a method get_status():

Returns a string like: "AC is ON - CustomBrand" or "Fan is OFF - CustomBrand" based on power_status.
"""


class SmartDevice:
    brand = "HomeTech"

    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status

        ## Shadowing the class attribute
        self.brand = "CustomBrand"

    def get_status(self):
        status = "On" if self.power_status else "Off"
        return f"{self.device_name} is {status} - {self.brand}"
    

device1 = SmartDevice("AC", True)
device2 = SmartDevice("Light", False)

print(device1.get_status())  # Output: AC is ON - CustomBrand
print(device2.get_status())  # Output: Light is OFF - CustomBrand