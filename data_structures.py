# List of integers
# numbers= [1,2,3,4,5,6]

# List of strings
# names= ["Aisha", "Kabira", "Tolu", "Hummul"]

# List of mixed data types
# mixed_list= [1, "Aisha", 3.14, True]

# print(mixed_list[-1])

# names.append("Zainab")  # Adding a new name to the list
# names.insert(2, "Fatima")  # Inserting a name at index 2
# print(names)
# names.remove("Tolu")  # Removing a name from the list
# print(names)
# names.pop()  # Removing the last name from the list
# print(names)

# numbers= [1,2,3,4,5,6]
# del numbers[2]
# print(numbers)

# fruits = ["apple", "banana", "cherry", "date"]
# sliced_fruits = fruits[1:3]  # This starts from index 1 and goes up to, but does not include, index 3
# print(sliced_fruits) 

# sets 
# set1={1, 2, 3, 4, 5}
# set2={4, 5, 6, 7, 8}
# Union of two sets
# print (set1| set2) 
# intersection  
# print(set1 & set2) 
# Difference of two sets
#print(set1 - set2)  # Elements in set1 but not in set2

# Manipulating Dictionaries
# info= {
#     "name": "Aisha",
#     "age": 25,
#     "city": "Lagos"
# }
# info["country"] = "Nigeria"  # Adding a new key-value pair
# info["age"] = 26  # Updating the value of an existing key
# print(info)
# # Deleting a key-value pair
# del info["city"]  # Removing the key "city" and its value
# if "age" in info:  # Checking if a key exists
#     del info["age"]  # Removing the key "age" if it exists
# print(info)
# info["age"]=24
# print(info)

#word frequency counter
sentence = input ("Enter a sentence: ")
#Split sentence into words
words= sentence.split()
# Create an empty dictionary to store word counts
word_count = {}
# Count the frequency of each word
for word in words:
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


