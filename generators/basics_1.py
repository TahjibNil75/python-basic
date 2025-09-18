# Regular Function

def regular_function():
    return "This is a regular function."


def generator_function():
    yield "This is a generator function."
    yield "It can yield multiple values."
    yield "You can iterate over it like a list."

return_value = generator_function()
print(next(return_value))
print(next(return_value))
print(next(return_value))
# print(next(return_value))