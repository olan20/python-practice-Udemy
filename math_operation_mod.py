def addition (a,b):
    return a+b

def subtraction (a,b):
    return a-b

def multiplication (a,b):
    return a*b

def division (a,b):
    if b != 0:
        return a/b
    else:
        return "Division by zero is not allowed"
    
    #to check if a number is even or odd 

def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
