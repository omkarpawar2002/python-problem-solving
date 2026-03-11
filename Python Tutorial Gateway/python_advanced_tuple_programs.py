# Get Tuple Items
'''
t = (10,20,30,40,50)
for i in t:
    print(i)
'''

# Python Program to Print Tuple using string formatting
'''
t = (10,20,30,40,50)
print(f"This is a tuple : {t}")
'''

# Python Program to Print Even Numbers in Tuple
'''
t = (1,2,3,4,5,6,7,8,9,10)
for i in t:
    if(i % 2 == 0):
        print(i)
'''

# Python Program to Print Negative Numbers in Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
for i in t:
    if(i < 0):
        print(i)
'''

# Python Program to Print Positive Numbers in Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
for i in t:
    if(i > 0):
        print(i)
'''

# Python Program to Print Odd Numbers in Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
for i in t:
    if(i % 2 != 0):
        print(i)
'''

# Python Program to Print Smallest Item in a Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
print(f"Smallest Item : {min(t)}")
'''

# Python Program to Print Largest Item in a Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
print(f"Largest Item : {max(t)}")
'''

# Python Program to Find Largest and Smallest Item in a Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
smallest = largest = t[0]
for i in range(len(t)):
    if(t[i] > largest):
        largest = t[i]
    if(t[i] < smallest):
        smallest = t[i]
print(f"Smallest Item : {smallest}")
print(f"Largest Item : {largest}")
'''

# Python Program to Print Tuple Items
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
for i in t:
    print(i)
'''