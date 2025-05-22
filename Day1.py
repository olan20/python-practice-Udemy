# #determining if a condition is true or false
# num=-20
# if num>0:
#     print("Number is Positive")
# elif num==0:
#     print("Number is Zero")
# else:
#     print("Number is Negative")
#     #Nested conditions 
#     age=45   
#     if age>20:
#         if age <35: 
#             print("Young Adult")
#         else:
#             print("Adult")    

# #Syntax for for-loop through a list of items 
# fruits=["apple","banana","cherry"]
# for x in fruits:
#     print(x)

# #Loop with range 
# #for i in range(7):
#    # print(i)

# #while-loop 
# #count down for 6 
# count=6
# while count>0:
#     print(count)
#     count-=1
# print ("outside while loop")

# #break statement- to terminate a loop when a condition is met
# for i in range(7):
#     if i==4:
#         break
#     print(i)

# #continue statement- to skip the current iteration and continue with the next
# for i in range(7):
#     if i==4:
#         continue
#     print(i)

# for i in range (10):
#     if i %2 == 0:
#         continue
#     print(i)


#CHECK if a number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int (num**0.5)+1 ):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
