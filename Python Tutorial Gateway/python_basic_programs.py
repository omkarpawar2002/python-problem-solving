# Python program for Hello World
'''
print("Hello World")
'''

# Python program to add Two Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
add_two_number = num1 + num2
print(f"Sum of {num1} and {num2} : {add_two_number}")
'''

# Python program to subtract two numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
subtract_two_number = num1 - num2
print(f"Subtract of {num1} and {num2} : {subtract_two_number}")
'''

# Python Program to Multiply Two numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
multiply_two_number = num1 * num2
print(f"Multiply of {num1} and {num2} : {multiply_two_number}")
'''

# Python program for Arithmetic Operations
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

add_two_number = num1 + num2
subtract_two_number = num1 - num2
multiply_two_number = num1 * num2
divide_two_number = num1 / num2
floor_divide_two_number = num1 // num2
power_of_two_number = num1 ** num2
modulo_two_number = num1 % num2

print(f"Addition of {num1} and {num2} : {add_two_number}")
print(f"Subtraction of {num1} and {num2} : {subtract_two_number}")
print(f"Multiply of {num1} and {num2} : {multiply_two_number}")
print(f"Division of {num1} and {num2} : {divide_two_number}")
print(f"Floor Division of {num1} and {num2} : {floor_divide_two_number}")
print(f"Power of {num1} and {num2} : {power_of_two_number}")
print(f"Modulo of {num1} and {num2} : {modulo_two_number}")
'''

# Python program to print Calendar
'''
import calendar

year = int(input("Enter any year : "))
month = int(input("Enter any month : "))
result = calendar.month(year,month)
print(result)
'''

# Python program to find Largest of 2 Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 > num2):
    print(f"{num1} is greater than {num2}")
elif(num2 > num1):
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
'''

# Python program to find Largest of 3 Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
largest = max(num1,num2,num3)
print(f"Largest number is : {largest}")
'''

# Python program for Leap Year
'''
year = int(input("Enter any year : "))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''

# Python Program to Print Negative Numbers in a Range
'''
start = int(input("Enter starting point : "))
end = int(input("Enter ending point : "))
for i in range(start,end+1):
    if(i < 0):
        print(i)
'''


# Python Program to Print Positive Numbers in a Range
'''
start = int(input("Enter starting point : "))
end = int(input("Enter ending point : "))
for i in range(start,end):
    if(i > 0):
        print(i)
'''

# Python program to find Positive or Negative
'''
number = int(input("Enter any number : "))
if(number > 0):
    print(f"{number} is a positive number")
elif(number < 0):
    print(f"{number} is a negative number")
else:
    print(f"{number} is a Zero")
    
'''

# Python program to check Number Divisible by 5 and 11
'''
num = int(input("Enter any number : "))
if((num % 5 == 0) and (num % 11 == 0)):
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")
'''

# Python Program to Find the Sum and Average Of Three Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
total = num1 + num2 + num3
average = total / 3
print(f"Total of 3 numbers are : {total} \nAverage of 3 numbers are : {average}")
'''

# Python Program to Find the Average Of Two Numbers
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
total = num1 + num2 
average = total / 2
print(f"Average of 2 numbers are : {average}")
'''

# Python Program to Get Current Date and Time
'''
import datetime

today = datetime.datetime.today()
print(today)
'''