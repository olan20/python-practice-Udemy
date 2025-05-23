#local scope 
def greet():
    message= "Good Morning"
    print(message)
greet()

#Global scope 
greeting="Hello"
def say_hello():
    print(greeting + " from inside the function")

say_hello()
print(greeting+ " from outside the function")


