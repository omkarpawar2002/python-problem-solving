# Python Program to do Arithmetic Calculations using Functions
'''
def add(num1 , num2):
    addition = num1 + num2
    return addition

def sub(num1 , num2):
    subtraction = num1 - num2
    return subtraction

def mul(num1 , num2):
    multiplication = num1 * num2
    return multiplication

def div(num1 , num2):
    division = num1 / num2
    return division

while True:
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    choice = int(input("** Enter your choice : **"\
                       "\n 1.Addition "\
                       "\n 2.Subtraction "\
                       "\n 3.Multiplication "\
                       "\n 4.Division "\
                       "\n 5.Exit : "))
    if(choice == 1):
        result = add(number1,number2)
        print(f"Addition of {number1} and {number2} is : {result}")
    elif(choice == 2):
        result = sub(number1,number2)
        print(f"Subtraction of {number1} and {number2} is : {result}")
    elif(choice == 3):
        result = mul(number1,number2)
        print(f"Multiplication of {number1} and {number2} is : {result}")
    elif(choice == 4):
        result = div(number1,number2)
        print(f"Division of {number1} and {number2} is : {result}")
    elif(choice == 5):
        break
    else:
        print("Incorrect Choice")
'''
    
# Python Program to Count Number of Digits in a Number
'''
number = int(input("Enter any number : "))
print(f"Total Number of digits in {number} are : {len(str(number))}")
'''

# Python Program to find Factors of a Number
'''
number = int(input("Enter any number : "))
number_factors = []
for ele in range(1,number+1):
    if(number % ele == 0):
        number_factors.append(ele)
print(f"Number {number} Factors Are : {number_factors}")
'''

# Python Program to find the Factorial of a Number
'''
number = int(input("Enter any number : "))
fact = 1
for ele in range(1,number+1):
    fact = fact * ele
print(f"Factorial Of {number} are : {fact}")
'''

# Python program to print the First Digit of a Number
'''
number = int(input("Enter any number : "))
print(f"First Digit Of Number {number} are : {str(number)[0]}")
'''

# Python program to print Last Digit in a Number
'''
number = int(input("Enter any number : "))
print(f"Last Digit Of Number {number} are : {str(number)[-1]}")
'''

# Python program to find the GCD of Two Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num1_divisor = []
num2_divisor = []
for i in range(1,num1+1):
    if(num1 % i == 0):
        num1_divisor.append(i)
for i in range(1,num2+1):
    if(num2 % i == 0):
        num2_divisor.append(i)
print(num1_divisor)
print(num2_divisor)
s1 = set(num1_divisor)
s2 = set(num2_divisor)
print(f"Greatest Common Divisor Are : {max(s1.intersection(s2))}")
'''

# Python program to find LCM of Two Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num1_multiple = []
num2_multiple = []
for i in range(1,11):
    num1_multiple.append(num1*i)
    num2_multiple.append(num2*i)
print(num1_multiple)
print(num2_multiple)
s1 = set(num1_multiple)
s2 = set(num2_multiple)
print(f"LCM of Two Numbers {num1} and {num2} are : {min(s1.intersection(s2))}")
'''

# Python program to check a Palindrome Number
'''
number = int(input("Enter any number : "))
number_str = str(number)
if(number_str == number_str[::-1]):
    print(f"{number_str} is a Palindrome Number")
else:
    print(f"{number_str} is not a Palindrome Number")
'''

# Python Program to Print Palindrome Numbers from 1 to 100
'''
for number in range(1,101):
    if(str(number) == str(number)[::-1]):
        print(number)
'''

# Python Program to Reverse a Number
'''
number = int(input("Enter any number : "))
number_str = str(number)
print(f"Original Number  : {number_str}")
print(f"Reverse Number  : {number_str[::-1]}")
'''

# Python program to find the Sum of Digits in a Number
'''
number = int(input("Enter any number : "))
number_str = str(number)
sum_of_digits = 0
for i in number_str:
    sum_of_digits = sum_of_digits + int(i)
print(f"Sum of digits are : {sum_of_digits}")
'''

# Python Program to Swap Two Numbers
'''
n1 = 10
n2 = 12
print(f"N1 : {n1}")
print(f"N2 : {n2}")
n1 , n2 = n2 , n1
print(f"N1 : {n1}")
print(f"N2 : {n2}")
'''