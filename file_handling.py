# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
#List comprehensive
#expression for items in iterable if condition

from functools import reduce

# create a list of squares
sqr= [x**2 for x in range(10)]
print(sqr)

#filter even numbers
evens = [x for x in range(20) if x % 2 == 0]
print (evens)

odds = [x for x in range(20) if x % 2 != 0]
print (odds)

#Lambda functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
add = lambda x, y: x + y
print(add(5, 3))

numbers = [1, 2, 3, 4, 5]
squares= map(lambda x: x**2, numbers)
print (list(squares))


# Filter even numbers using lambda
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

#reduce func
product = reduce(lambda x, y: x * y, numbers)
print(product)