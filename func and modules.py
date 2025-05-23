# #local scope 
# def greet():
#     message= "Good Morning"
#     print(message)
# greet()

# #Global scope 
# greeting="Hello"
# def say_hello():
#     print(greeting + " from inside the function")

# # say_hello()
# # print(greeting+ " from outside the function")

# # #importing modules
# import math
# print(math.sqrt(25))
# #Using aliases 
# import math as m
# print(m.sqrt(36))


#import a specific function from a module
# from math import sqrt
# print(sqrt(72))

#Creating a func to cal a factorial 

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# def print_factorial(n):
#     result = factorial(n)
#     print ("The factorial of", (n), "is", (result))  

# print_factorial(10)

#Build a custom module
import math_operation_mod as mod

num1= 4
num2=0

# print("Addition:", mod.addition(num1,num2))
# print("Subtraction:", mod.subtraction(num1,num2))
# print("Multiplication:", mod.multiplication(num1,num2))     
# print("Division:", mod.division(num1,num2))

print(mod.check_even_odd(num1))
print(mod.check_even_odd(num2))
