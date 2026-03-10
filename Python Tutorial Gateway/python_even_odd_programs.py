# Python Program to find Odd or Even
'''
num = int(input("Enter any number : "))
if(num % 2 == 0):
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")
'''

# Python program to Print Natural number 1 to N
'''
num = int(input("Enter any number : "))
for i in range(1,num+1):
    print(i)
'''

# Python program to Print Natural Numbers in Reverse Order
'''
start = int(input("Enter starting number : "))
for i in range(start,0,-1):
    print(i)
'''

# Python program to Print Even Numbers from 1 to 100
'''
for i in range(1,101):
    if(i % 2 == 0):
        print(i)
'''

# Python program to print Odd Numbers from 1 to 100
'''
for i in range(1,101):
    if(i % 2 != 0):
        print(i)
'''

# Python Program to Print First 10 Even Natural Numbers
'''
for i in range(2,21,2):
    print(i)
'''

# Python Program to Print First 10 Natural Numbers
'''
for i in range(1,11):
    print(i)
'''

# Python Program to Print First 10 Natural Numbers in Reverse
'''
for i in range(10,0,-1):
    print(i)
'''

# Python Program to Print First 10 Odd Natural Numbers
'''
count = 0
for i in range(1,100):
    if(i % 2 != 0):
        if(count < 10):
            print(i)
            count += 1
'''

# Python Program to find the Sum and Average of Natural Numbers
'''
total = average = count =  0
for i in range(1,11):
    total += i
    count += 1
average = total / count

print(f"Total of {count} number are : {total} \nAverage is {average}")
'''

# Python Program to Read 10 Numbers and Find their Sum and Average
'''
total = average = count = 0
while count < 10:
    num = int(input("Enter any number : "))
    total += num
    count += 1
average = total / count

print(f"Total of {count} number are : {total} \nAverage is {average}")
'''

# Python Program to Find the Sum of 10 Numbers and Skip Negative Numbers
'''
total = count = 0
while count < 10:
    num = int(input("Enter any number : "))
    count += 1
    if(num < 0):
        continue
    total += num
    
print(f"Total of {count} number are : {total}")
'''

# Python Program to Find the Sum of 10 Numbers until user enters Positive Numbers
'''
total = count = 0
while count < 10:
    num = int(input("Enter any number : "))
    if(num > 0):
        total += num
        count += 1
print(f"Total is {total}")
'''

# Python Program to find Sum of Natural Numbers
'''
total = 0
for i in range(1,101):
    total += i
print(f"Sum of natural number : {total}")
'''

# Python Program to find Sum of Even Numbers
'''
total = 0
for i in range(1,101):
    if(i % 2 == 0):
        total += i
print(f"Sum of Even number : {total}")
'''

# Python Program to find the Sum and Average of Natural Numbers
'''
total = count = 0
for i in range(1,101):
    total += i
    count += 1
average = total / count
print(f"Sum of natural number : {total} \nAverage of natural number : {average}")
'''

# Python Program to find the Sum of Odd Numbers
'''
total = 0
for i in range(1,101):
    if(i % 2 != 0):
        total += i
print(f"Sum of Odd number : {total}")
'''

# Python Program to find the sum of Even and Odd Numbers
'''
sum_of_even = sum_of_odd = 0
for i in range(1,101):
    if(i % 2 == 0):
        sum_of_even += i
    else:
        sum_of_odd += i
print(f"Sum of Even number : {sum_of_even}")
print(f"Sum of Odd number : {sum_of_odd}")
'''

# Python Program to Read 10 Numbers and Find their Sum and Average
'''
total = count = 0
while count < 10:
    num = int(input("Enter any number : "))
    total += num
    count += 1
average = total / count
print(f"Total is : {total} \nAverage is : {average}")
'''