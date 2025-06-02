# first= "Hello"
# second = "World"
# result= first + " " + second
# print(result)

# text= "Python is a programming language"
# print(text[0:9])
# print(text[-12:])

# name= "Aisha" 
# age=40
# print(f"My name is {name} and i am {age} years old") #curly brackets are used for variables

#common string methods are split, join, replace, strip
#Split 
# text = "Python is a programming language"
# words = text.split()
# print(words)

# #join
# new_text= "/".join(words)
# print(new_text)
# updated_text= text.replace("Python", "Java")
# print(updated_text)

# #strip
# messy_text = "   Hello, World!   "
# print(messy_text)
# cleaned_text = messy_text.strip()
# print(cleaned_text)


import re

# text= "You can contact me at 092-123-4567" 
# digits=re.findall(r"\d+", text)
# print(digits)
# #replacing the texts 
# updated_text=re.sub(r"\d", "X", text)
# print(updated_text)

# #program to clean texts

# def new_text(text):
#    #remove punc 
#    text= re.sub(r"[^\w\s]", "", text)  
#    #remove extra spaces
#    text=" ".join(text.split())
#    #convert to lowercase
#    return text.lower()
   
# message = input ("Enter a message: ")
# cleaned_message = new_text(message)
# print("Cleaned message:", cleaned_message)

#to det if a string is a palindrome
# def is_palindrome(text):
#     text="".join(char.lower() for char in text if char.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
#     return text == text[::-1]  # Check if the cleaned text is equal to its reverse

# message = input("Enter a sentence: ")
# if is_palindrome(message):
#     print(f"'{message}' is a palindrome.")
# else:
#     print(f"'{message}' is not a palindrome.")

# to count the number of vowels in a string
# def count_unique_vowels(text):
#     vowels = "aeiou"
#     count = set(char for char in text.lower() if char in vowels)
#     return len(count)

# find_vowels = input("Enter a sentence: ")
# vowel_count = count_unique_vowels(find_vowels)
# print(f"The number of vowels in '{find_vowels}' is: {vowel_count}")

#to find and replace emails 
text= "contact me at jessiej@gmail.com"
email= re.findall(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b", text)
print("Email found:", email)
updated_text=re.sub(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b", "[email hidden]", text)
print(updated_text)