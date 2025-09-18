from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


@log_activity
def brew_coffee(coffe_type, milk="yes", sugar="no"):
    print(f"Brewing {coffe_type} with milk: {milk}, sugar: {sugar}")


brew_coffee("Espresso")