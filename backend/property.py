class User:
    def __init__(self, username,email, age):
        self._username = username
        self._email = email
        self._age = age

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        if len(value) >= 4:
            self._username = value
        else:
            print("Username must be at least 4 characters long")

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" in value and "." in value:
            self._email = value
        else:
            print("Invalid email format")

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age must be a non-negative integer")

    @property
    def info(self):
        return f"Username: {self._username}, Email: {self._email}, Age: {self._age}"
    


user1 = User("tahjib", "tahjib@gmail.com", 25)

user1.username = "ta"
user1.email = "tahjibgmail.com"
user1.age = -5
print(user1.username)
print(user1.email)
print(user1.age)
print(user1.info)

