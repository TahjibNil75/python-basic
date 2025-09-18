class UserAlreadyExistError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

class InvalidEmailError(Exception):
    pass


class UserService:
    def __init__(self):
        self.users = {}  # pretend database {email: password}

    def registerUser(self, email, password):
        try:
            if email in self.users:
                raise UserAlreadyExistError(f"User with {email} already existed")
            if "@" not in email or "." not in email:
                raise InvalidEmailError("Invalid email")
            if len(password) < 5:
                raise WeakPasswordError("password must 6 character long")
            
            self.users[email] = password
            print(f"User with {email} created")
            
        except UserAlreadyExistError as e:
            print(f"Registration Failed: {e}")
        except InvalidEmailError as e:
            print(f"Registration Failed: {e}")
        except WeakPasswordError as e:
            print(f"Registration Failed: {e}")
        except Exception as e:
            print(f"Unexpected error {e}")

        else:
            print("Registration Done!! \n")
        
        finally:
            print("📌")

if __name__ == "__main__":
    service = UserService()

    print("First User:")
    service.registerUser("tahjib@gmail.com", "ghjklp")

    print("Second User:")
    service.registerUser("tahjib", "hjjkguyy")

    print("Third User:")
    service.registerUser("tahjib@gmail.com", "123456")

    print("Fourth User:")
    service.registerUser("tah@gmail.com", "123")


