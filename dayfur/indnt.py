"""def separateFunction(b):
    for i in b:
        if i ==1:
            return True
    return False


separateFunction([2,3,5,6,1])
"""
def greet(name, greeting="Hello"):
    """Print a greeting to the user `name`Optional parameter `greeting` can change what they're greeted with."""
    print("{} {}".format(greeting, name))
    
help(greet)