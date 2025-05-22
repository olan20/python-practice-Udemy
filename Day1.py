# # #determining if a condition is true or false
# # num=-20
# # if num>0:
# #     print("Number is Positive")
# # elif num==0:
# #     print("Number is Zero")
# # else:
# #     print("Number is Negative")
# #     #Nested conditions 
# #     age=45   
# #     if age>20:
# #         if age <35: 
# #             print("Young Adult")
# #         else:
# #             print("Adult")    

# # #Syntax for for-loop through a list of items 
# # fruits=["apple","banana","cherry"]
# # for x in fruits:
# #     print(x)

# # #Loop with range 
# # #for i in range(7):
# #    # print(i)

# # #while-loop 
# # #count down for 6 
# # count=6
# # while count>0:
# #     print(count)
# #     count-=1
# # print ("outside while loop")

# # #break statement- to terminate a loop when a condition is met
# # for i in range(7):
# #     if i==4:
# #         break
# #     print(i)

# # #continue statement- to skip the current iteration and continue with the next
# # for i in range(7):
# #     if i==4:
# #         continue
# #     print(i)

# # for i in range (10):
# #     if i %2 == 0:
# #         continue
# #     print(i)


# #CHECK if a number is prime or not
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, int (num**0.5)+1 ):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# #Menu Driven Calculator 
def add (x,y):
    return x+y  
def subtract (x,y): 
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    if b!=0:
        return x/y
    else:
        return "Division by zero is not allowed"
    
while True:
    print("\nMenu Driven Calculator")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice =="5":
        print("Exiting the calculator")
        break
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice, please try again")
        continue

    num1 = float(input("Enter first number: "))
    num2=float(input("Enter second number:"))

    if choice== "1":
        print("Result=",add(num1,num2))
    elif choice=="2":
        print("Result:", subtract(num1,num2))
    elif choice=="3":             
        print("Result:", multiply(num1,num2))
    elif choice=="4":
        print("Result:", divide(num1,num2))
    else:
        print("Invalid choice, please try again")



