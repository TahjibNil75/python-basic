from functools import wraps

def auth_required(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            raise PermissionError (f"You do not have permission to access this resource as {user_role}.")
        return func(user_role)
    return wrapper

@auth_required
def access_inventory(role):
    print(f"Accessing inventory as {role}.")


access_inventory("admin")  
# access_inventory("user")  