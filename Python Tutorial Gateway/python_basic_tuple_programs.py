# Python Program to add an Item to a tuple
'''
t = (10,20,30,40)
print(f"Original Tuple : {t}")
li = list(t)
li.append(101)
t = tuple(li)
print(f"Modified Tuple : {t}")
'''

# Python Program to create a Tuple
'''
t = (10,20,30,40,50,60)
print(t)
'''

# Python Program to create Tuple of Different Types
'''
t = (10,20,"welcome",True)
print(t)
'''

# Python Program to Find Tuple Length
'''
t = (10,20,"welcome",True)
print(f"Length of tuple : {len(t)}")
'''

# Python Program to Remove an Item from Tuple
'''
t = (10,20,"welcome",True)
print(f"Original Tuple : {t}")
li = list(t)
li.remove("welcome")
t = tuple(li)
print(f"Modified Tuple : {t}")
'''

# Python Program to Slice a Tuple
'''
t = (10,20,"welcome",True)
print(t[1:3])
'''

# Python Program to Unpack Tuple Items
'''
t = (10,20,"welcome",True)
print(t)
a , b , c , d = t
print(a)
print(b)
print(c)
print(d)
'''

# Python Program to Create a Tuple with Numbers
'''
t = (10,20,30,40,50)
print(t)
'''

# Python Program to Check Item exists in Tuple
'''
t = (10,20,"welcome",True)
print(t)
item1 = 20
item2 = 87
print(item1 in t)
print(item2 in t)
'''

# Python Program to Find Sum of Even and Odd Numbers in Tuple
'''
t = (1,2,3,4,5,6,7,8,9,10)
sum_of_even = sum_of_odd = 0
for i in t:
    if(i % 2 == 0):
        sum_of_even += i
    else:
        sum_of_odd += i
print(f"Sum of Even Number : {sum_of_even}")
print(f"Sum of Odd Number : {sum_of_odd}")
'''

# Python Program to Find Sum of Tuple Items
'''
t = (1,2,3,4,5,6,7,8,9,10)
print(f"Sum of tuple : {sum(t)}")
'''

# Python Program to Reverse Tuple
'''
t = (1,2,3,4,5,6,7,8,9,10)
print(f"Original Tuple : {t}")
print(f"Reversed Tuple : {t[::-1]}")
'''

# Count Positive and Negative Numbers in a Tuple
'''
t = (1,2,3,4,5,6,7,-8,9,-10)
positive = negative = 0
for i in t:
    if(i < 0):
        negative += 1
    elif(i > 0):
        positive += 1
print(f"Positive Number : {positive}")
print(f"Negative Number : {negative}")
'''

# Count Even and Odd Numbers in Tuple
'''
t = (1,2,3,4,5,6,7)
count_even = count_odd = 0
for i in t:
    if(i % 2 == 0):
        count_even += 1
    else:
        count_odd += 1
print(f"Total Even Numbers Are : {count_even}")
print(f"Total Odd Numbers Are : {count_odd}")
'''