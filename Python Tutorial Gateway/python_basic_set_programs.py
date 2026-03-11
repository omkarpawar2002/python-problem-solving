# Python Program to create a Set
'''
s = {10,20,30,40}
print(s)
'''

# Python program to Count Even and Odd Numbers in Set
'''
s = {1,2,3,4,5,6,7,8,9}
count_even = count_odd = 0
for i in s:
    if(i % 2 == 0):
        count_even += 1
    else:
        count_odd += 1
print(f"Count Even Numbers : {count_even}")
print(f"Count Odd Numbers : {count_odd}")
'''

# Python program to Count Positive and Negative Numbers in Set
'''
s = {1,2,3,4,5,6,7,-8,9,-10}
positive = negative = 0
for i in s:
    if(i < 0):
        negative += 1
    elif(i > 0):
        positive += 1
print(f"Positive Number : {positive}")
print(f"Negative Number : {negative}")
'''

# Python program to Iterate Set Items
'''
s = {10,20,30,40,50}
for i in s:
    print(i)
'''

# Python program to Print Largest Set Item
'''
s = {10,20,30,40,50}
print(f"Largest Set Item : {max(s)}")
'''

# Python program to find Length of a set
'''
s = {10,20,30,40,50}
print(f"Length of set : {len(s)}")
'''

# Python program to Print Even Numbers in Set
'''
s = {11,12,13,14,15}
for i in s:
    if(i % 2 == 0):
        print(i)
'''

# Python program to Print Negative Numbers in Set
'''
s = {1,2,3,4,5,6,7,-8,9,-10}
for i in s:
    if(i < 0):
        print(i)
'''

# Python program to Print Odd Numbers in Set
'''
s = {1,2,3,4,5,6,7,-8,9,-10}
for i in s:
    if(i % 2 != 0):
        print(i)
'''

# Python program to Print Positive Numbers in Set
'''
s = {1,2,3,4,5,6,7,-8,9,-10}
for i in s:
    if(i > 0):
        print(i)
'''

# Python program to find Sum of Even and Odd Numbers in Set
'''
s = {1,2,3,4,5,6,7,8,9,10}
sum_of_even = sum_of_odd = 0
for i in s:
    if(i % 2 == 0):
        sum_of_even += i
    else:
        sum_of_odd += i
print(f"Sum of Even Number : {sum_of_even}")
print(f"Sum of Odd Number : {sum_of_odd}")
'''

# Python program to find Smallest Set Item
'''
s = {10,20,30,40,50}
print(f"Smallest Set Item : {min(s)}")
'''