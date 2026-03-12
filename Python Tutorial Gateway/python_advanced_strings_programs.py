# Python program to Count the Occurrence of a Character in a String
'''
string_input = input("Enter any string : ")
char = input("Enter any character : ")
print(f"{char} Occurs {string_input.count(char)} times in a String.")
'''

# Python Program to Count Character Frequency in a String
'''
string_input = input("Enter any string : ")
char_frequency = {}
for char in string_input:
    if(char not in char_frequency):
        char_frequency[char] = 1
    else:
        char_frequency[char] += 1
print(f"Character Frequency : {char_frequency}")
'''

# Python program to Count Total Characters in a String
'''
input_string = input("Enter string input : ")
print(f"Total {len(input_string)} characters in string")
'''

# Python program to Count the Total Number of Words in a String
'''
input_string = input("Enter string input : ").split()
print(f"Total {len(input_string)} words in string")
'''

# Python program to Count Vowels in a String
'''
input_string = input("Enter string input : ").lower()
count_vowel = 0
for char in input_string:
    if(char in 'aeiou'):
        count_vowel += 1
print(f"Total {count_vowel} Vowels In String")
'''

# Python program to Count Vowels and Consonants in a String
'''
input_string = input("Enter string input : ").lower()
count_vowel = count_consonant = 0
for char in input_string:
    if(char in 'aeiou'):
        count_vowel += 1
    elif(char >= 'a' and char <= 'z'):
        count_consonant += 1
print(f"Total {count_vowel} Vowels In String")
print(f"Total {count_consonant} Consonants In String")
'''

# Python program to Count Alphabets Digits and Special Characters in a String
'''
input_string = input("Enter string input : ").lower()
count_alphabet = count_digit = count_special_symbol = 0
for char in input_string:
    if(char.isalpha()):
        count_alphabet += 1
    elif(char.isdigit()):
        count_digit += 1
    else:
        count_special_symbol += 1
print(f"Total {count_alphabet} alphabets In String")
print(f"Total {count_digit} digits In String")
print(f"Total {count_special_symbol} special symbols In String")
'''

# Python program to Replace Blank Space with Hyphen in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
new_string = input_string.replace(' ','-')
print(f"New String : {new_string}")
'''

# Python program to Replace Characters in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
char = input("Enter any character : ")
new_string = input_string.replace(char,'@')
print(f"New String : {new_string}")
'''

# Python program to Remove Odd Characters in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
new_string = ''
for index,char in enumerate(input_string):
    if(index % 2 == 0):
        new_string += char
print(f"New String : {new_string}")
'''

# Python program to Remove Odd Index Characters in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
new_string = ''
for index,char in enumerate(input_string):
    if(index % 2 == 0):
        new_string += char
print(f"New String : {new_string}")
'''

# Python program to Remove the First Occurrence of a Character in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
character = input("Enter character you want to remove : ")
new_string_list = [char for char in input_string]
new_string_list.remove(character)
print(f"New String : {''.join(new_string_list)}")
'''

# Python program to Remove Last Occurred Character in a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
character = input("Enter character you want to remove : ")
new_string_list = [char for char in input_string]
new_string_list.reverse()
new_string_list.remove(character)
new_string_list.reverse()
print(f"New String : {''.join(new_string_list)}")
'''

# Python Program to Remove Punctuations from a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
new_string = ''
for char in input_string:
    if(char.isalpha() or char.isdigit() or char.isspace()):
        new_string += char
print(f"New Updated String : {new_string}")
'''

# Python program to Reverse a String
'''
input_string = input("Enter any string : ")
print(f"Original String : {input_string}")
print(f"Reversed String : {input_string[::-1]}")
'''