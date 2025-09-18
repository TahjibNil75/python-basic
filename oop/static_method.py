## - static Methods = Best for utility functions that do not need access to class data. 
# Dont need to creat object from that class

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}."
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions
    

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Chef")

print(emp1.get_info())

print(f"Is 'Manager' a valid position? {Employee.is_valid_position('Manager')}")
print(f"Is 'Chef' a valid position? {Employee.is_valid_position('Chef')}")

print(emp2.is_valid_position("Chef"))  # Not recommended but works