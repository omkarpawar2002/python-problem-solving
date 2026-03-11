# Python Program to Add Key-Value Pair to a Dictionary
'''
user_details = {
    'name':'joe',
    'age':23
}
print(f"Original Dictionary : {user_details}")
user_details["username"] = 'joe_123'
print(f"Modified Dictionary : {user_details}")
'''

# Python program to Check if a Given key exists in a Dictionary
'''
user_details = {
    'name':'joe',
    'age':23
}
print(f"Original Dictionary : {user_details}")
print("location" in user_details)
print("age" in user_details)
'''

# Python program to Count words in a String using Dictionary
'''
input_data = input("Enter anything : ")
count_word = {}
input_data = input_data.split()
for word in input_data:
    if(word not in count_word):
        count_word[word] = 1
    else:
        count_word[word] += 1
print(count_word)
'''

# Python program to Create Dictionary of keys from 1 to n and values are square of keys
'''
n = int(input("Enter input data : "))
squares = {}
for i in range(1,n+1):
    squares[i] = i**2
print(squares)
'''

# Python program to Create Dictionary of Numbers 1 to n in (x, x*x) form
'''
n = int(input("Enter input data : "))
squares = {}
for i in range(1,n+1):
    squares[i] = i**2
print(squares)
'''

# Python program to Map two lists into a Dictionary
'''
keys = [1,2,3,4,5]
values = ["one","two","three","four","five"]
result = dict(zip(keys,values))
print(result)
'''

# Merge Two Dictionaries
'''
user_details = {
    'name':'joe',
    'age':23
}
print(f"Original Dictionary : {user_details}")
user_info = {
    'username':'Bellion',
    'password':'Joe@123'
}
user_details.update(user_info)
print(f"Updated Dictionary : {user_details}")
'''

# Multiply All Items in a Dictionary
'''
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
keys = values = 1
for key,value in d.items():
    keys *= key
    values *= value
print(f"Multiplication of keys : {keys}")
print(f"Multiplication of values : {values}")
'''

# Remove Given Key from a Dictionary
'''
user_details = {
    'name':'joe',
    'age':23
}
print(f"Original Dictionary : {user_details}")
user_details.pop('name')
print(f"Modified Dictionary : {user_details}")
'''

# Sum of Items in a Dictionary
'''
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
keys = values = 0
for key,value in d.items():
    keys += key
    values += value
print(f"Sum of keys : {keys}")
print(f"Sum of values : {values}")
'''