# Python Program for ASCII Value of a Single Character
'''
character = input("Enter any character : ")
print(f"ASCII value of {character} is : {ord(character)}")
'''

# Python program to print ASCII Value of Total Characters in a String
'''
input_data = input("Enter any string : ")
ascii_char = {}
for i in input_data:
    ascii_char[i] = ord(i)
print(f"ASCII value of each character : {ascii_char}")
'''

# Python program to Concatenate Strings
'''
first_name = "joe"
last_name = "karlin"
print(first_name + ' ' + last_name)
'''

# Python program to Convert String to Uppercase
'''
input_string = input("Enter string : ")
print(input_string.upper())
'''

# Python program to Convert String to Lowercase
'''
input_string = input("Enter string : ")
print(input_string.lower())
'''

# Python program to Copy a String
'''
input_string = input("Enter string : ")
print(f"Original String : {input_string} and Id {id(input_string)}")
input_string_copy = input_string[:]
print(f"Copy String : {input_string_copy} and Id {id(input_string_copy)}")
'''

# Python program to check Palindrome or Not
'''
input_string = input("Enter string : ")
if(input_string == input_string[::-1]):
    print("String Are Palindrome")
else:
    print("String Are Not Palindrome")
'''

# Python Program to Check If Two Strings are Anagram
'''
string_1 = input("Enter first string : ")
string_2 = input("Enter second string : ")
string_1_char = {}
string_2_char = {}
for i in string_1:
    if(i not in string_1_char):
        string_1_char[i] = 1
    else:
        string_1_char[i] += 1
for i in string_2:
    if(i not in string_2_char):
        string_2_char[i] = 1
    else:
        string_2_char[i] += 1
if(string_1_char == string_2_char):
    print("String Are Anagram")
else:
    print("String Are Not Anagram")
'''

# Python program to Print the First Occurrence of a Character in a String
'''
string_input = input("Enter any input : ")
print(f"Original String : {string_input}")
char = input("Enter any character ")
print(f"{char} Occur At Index : {string_input.find(char)}")
'''

# Python program to Print the Last Occurrence of a Character in a String
'''
string_input = input("Enter any input : ")
print(f"Original String : {string_input}")
char = input("Enter any character ")
print(f"{char} Occur At Index : {string_input.rfind(char)}")
'''

# Python program to Print Characters in a String
'''
string_input = input("Enter any input : ")
for char in string_input:
    print(char)
'''

# Python program to find String Length
'''
string_input = input("Enter any string input : ")
print(f"Length of string : {len(string_input)}")
'''

# Total Occurrence of a Character in a string
'''
string_input = input("Enter any input : ")
char_count = {}
for char in string_input:
    if(char not in char_count):
        char_count[char] = 1
    else:
        char_count[char] += 1
print(char_count)
'''

# Toggle Characters Case
'''
string_input = input("Enter any input : ")
print(f"Original String : {string_input}")
print(f"Toggle String : {string_input.swapcase()}")
'''