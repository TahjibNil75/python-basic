#### Hiding Implementation Details ####

## You want to separate concerns: getting input, validating it and saving it
###### TASK ######
## - Write a register_user() that calls
#### - get_user_input()
## - validate_user_input()
## - save_user_data()


def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email



def validate_user_input(name, email):
    if not name or not email:
        raise ValueError("Name or email can not be empty.")
    if "@" not in email:
        raise ValueError("Invalid email format.")
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long.")
    if len(email) < 5:
        raise ValueError("Email must be at least 5 characters long.")
    return True


def save_user_data(name,email):
    with open("user_data_db.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}\n")
    print("User data saved successfully!") 





def register_user():
    try: 
        name, email = get_user_input()
        validate_user_input(name, email)
        save_user_data(name, email)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nRegistration process was interrupted by the user.")
    except EOFError:
        print("\nInput was interrupted. Please try again.")
    except FileNotFoundError:
        print("Error: The user data file could not be found. Please check the file path.")
    except IOError:
        print("Error: An I/O error occurred while trying to save user data. Please check your file permissions.")



register_user()
        