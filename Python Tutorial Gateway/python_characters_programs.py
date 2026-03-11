# Python program to check Alphabet or not
'''
character = input("Enter any character : ").lower()
if(character >= 'a' and character <= 'z'):
    print(f"{character} is an alphabet")
else:
    print(f"{character} is not alphabet")
'''

# Python program to check Alphabet or Digit
'''
character = input("Enter any character : ").lower()
if(character >= 'a' and character <= 'z'):
    print(f"{character} is an alphabet")
elif(character >= '0' and character <= '9'):
    print(f"{character} is digit")
else:
    print(f"{character} is not digit and not alphabet")
'''

# Python program to check Character is an Alphabet, Digit or Special Character
'''
character = input("Enter any character : ").lower()
if(character >= 'a' and character <= 'z'):
    print(f"{character} is an alphabet")
elif(character >= '0' and character <= '9'):
    print(f"{character} is digit")
else:
    print(f"{character} is special symbol")
'''

# Python program to check Digit or Not
'''
character = input("Enter any character : ")
if(character.isdigit()):
    print(f"{character} is digit")
else:
    print(f"{character} is not digit")
'''

# Python program to check Lowercase or not
'''
character = input("Enter any character : ")
if(character.islower()):
    print(f"{character} is in lowercase")
else:
    print(f"{character} is not in lowercase")
'''

# Python program to check Lowercase or Uppercase
'''
character = input("Enter any character : ")
if(character.islower()):
    print(f"{character} is in lowercase")
elif(character.isupper()):
    print(f"{character} is in uppercase")
else:
    print(f"{character} is not in lowercase and uppercase")
'''

# Python Program to check Uppercase or not
'''
character = input("Enter any character : ")
if(character.isupper()):
    print(f"{character} is in uppercase")
else:
    print(f"{character} is not in uppercase")
'''

# Python program to check Vowel or Consonant
'''
character = input("Enter any character : ")
li = ['a','e','i','o','u','A','E','I','O','U']
if(character in li):
    print(f"{character} is vowel")
elif((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')):
    print(f"{character} is consonant")
else:
    print(f"{character} is not and vowel and consonant")
'''
