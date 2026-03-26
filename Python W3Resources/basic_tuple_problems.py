# 1. Create a Tuple
# Write a Python program to create a tuple.
'''
t = (10,20,30,40,50)
print(t)
'''

# 2. Create a Tuple with Different Data Types
# Write a Python program to create a tuple with different data types.
'''
t = (10,34.53,"welcome",True)
print(t)
'''

# 3. Create a Tuple of Numbers and Print One Item
# Write a Python program to create a tuple of numbers and print one item.
'''
t = (10,20,30,40,50)
print(t[2])
'''

# 4. Unpack a Tuple into Several Variables
# Write a Python program to unpack a tuple into several variables.
'''
t = (10,20,30)
a , b , c = t
print(a)
print(b)
print(c)
'''

# 5. Add an Item to a Tuple
# Write a Python program to add an item to a tuple.
'''
t = (10,20,30,40)
print(f"Original Tuple : {t}")
li = list(t)
li.append(101)
t = tuple(li)
print(f"Updated Tuple : {t}")
'''

# 6. Convert a Tuple to a String
# Write a Python program to convert a tuple to a string.
'''
t = (10,20,30,40)
print(f"Original Tuple : {t}")
tuple_string = ''
for i in t:
    tuple_string += str(i)
print(f"Updated String : {tuple_string}")
'''

# 7. Get the 4th Element from the Last Element of a Tuple
# Write a Python program to get the 4th element from the last element of a tuple.
'''
t = (10,20,30,40,50,60,70,80,90,100)
print(t[-4])
'''

# 8. Create a Clone of a Tuple
# Write a Python program to create a clone of a tuple.
'''
t = (10,20,30,40,50,60,70,80,90,100)
print(f"Original Tuple : {t} with Id : {id(t)}")
copy_tuple = t[:]
print(f"Clone Tuple : {copy_tuple} with Id : {id(copy_tuple)}")
'''

# 9. Find Repeated Items in a Tuple
# Write a Python program to find repeated items in a tuple.
'''
t = (10,20,30,40,10)
d = {}
for i in t:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
for i,j in d.items():
    if(j > 1):
        print(f"Repeted Items : {i}")
'''

# 10. Check Whether an Element Exists Within a Tuple
# Write a Python program to check whether an element exists within a tuple.
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original Tuple : {t}")
print(20 in t)
print(203 in t)
'''

# 11. Convert a List to a Tuple
# Write a Python program to convert a list to a tuple.
'''
li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original List : {li}")
t = tuple(li)
print(f"Updated Tuple : {t}")
'''

# 12. Remove an Item from a Tuple
# Write a Python program to remove an item from a tuple.
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original Tuple : {t}")
li = list(t)
li.remove(20)
t = tuple(li)
print(f"Updated Tuple : {t}")
'''

# 13. Slice a Tuple
# Write a Python program to slice a tuple.
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original Tuple : {t}")
print(t[2::2])
'''

# 14. Find the Index of an Item in a Tuple
# Write a Python program to find the index of an item in a tuple.
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original Tuple : {t}")
print(t.index(20))
'''

# 15. Find the Length of a Tuple
# Write a Python program to find the length of a tuple.
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(len(t))
'''

# 16. Convert a Tuple to a Dictionary
# Write a Python program to convert a tuple to a dictionary.
'''
keys = (10,20,30)
values = ("ten","twenty","thirty")
d = dict(zip(keys,values))
print(d)
'''

# 17. Unzip a List of Tuples into Individual Lists
# Write a Python program to unzip a list of tuples into individual lists.
'''
li = [(1, 2), (3, 4), (8, 9)]
print(list(zip(*li)))
'''

# 18. Reverse a Tuple
# Write a Python program to reverse a tuple.
'''
t = (10,20,30,40,50)
print(f"Original Tuple : {t}")
print(f"Reversed Tuple : {t[::-1]}")
'''

# 19. Convert a List of Tuples into a Dictionary
# Write a Python program to convert a list of tuples into a dictionary.
'''
li = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for key,value in li:
    d.setdefault(key,[]).append(value)
print(d)
'''

# 20. Print Tuple with String Formatting
# Write a Python program to print a tuple with string formatting.
'''
t = (10,20,30,40)
print(f"This is a tuple : {t}")
'''

# 21. Replace the Last Value of Tuples in a List
# Write a Python program to replace the last value of tuples in a list.
'''
t = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Original Tuple : {t}")
new_li = []
for element in t:
    new_ele = list(element)
    new_ele[-1] = 100
    new_li.append(tuple(new_ele))
print(new_li)
'''

# 22. Remove Empty Tuple(s) from a List of Tuples
# Write a Python program to remove empty tuple(s) from a list of tuples.
'''
li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
li = [i for i in li if(i)]
print(li)
'''

# 23. Sort a Tuple by Its Float Element
# Write a Python program to sort a tuple by its float element.
'''
li = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(f"Original : {li}")
print(sorted(li,reverse=True))
'''

# 24. Count Elements in a List Until an Element is a Tuple
# Write a Python program to count the elements in a list until an element is a tuple.
'''
num = [10, 20, 30, (10, 20), 40]
count_ele = 0
for ele in num:
    if(type(ele) != tuple):
        count_ele += 1
    else:
        break
print(f"Total Elements : {count_ele}")
'''

# 25. Convert a Given String List to a Tuple
# Write a Python program to convert a given string list to a tuple.
'''
st = "python 3.0"
li = [i for i in st if(not i.isspace())]
print(tuple(li))
'''

# 26. Calculate the Product of Numbers in a Tuple
# Write a Python program to calculate the product of numbers in a tuple.
'''
t = (4, 3, 2, 2, -1, 18)
product = 1
for i in t:
    product *= i
print(f"Product - multiplying all the numbers of the said tuple : {product}")
'''

# 27. Calculate Average Value of Numbers in a Tuple of Tuples
# Write a Python program to calculate the average value of numbers in a tuple of tuples.




# 28. Convert a Tuple of String Values to a Tuple of Integer Values
# Write a Python program to convert a tuple of string values to a tuple of integer values.
'''
t = (('333', '33'), ('1416', '55'))
print(f"Original Tuple : {t}")
li = []
for element in t:
    new_li = []
    for ele in element:
        new_li.append(int(ele))
    li.append(tuple(new_li))
print(f"Updated Tuple : {tuple(li)}")
'''

# 29. Convert a Tuple of Positive Integers into an Integer
# Write a Python program to convert a tuple of positive integers into an integer.
'''
t = (1,2,3)
s = ''
for i in t:
    s += str(i)
print(int(s))
'''

# 30. Check if a Specified Element Appears in a Tuple of Tuples
# Write a Python program to check if a specified element appears in a tuple of tuples.
'''
t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
li = [j for i in t for j in i]
t = tuple(li)
print("White" in t)
print("Olive" in t)
'''

# 31. Compute Element-wise Sum of Given Tuples
# Write a Python program to compute the element-wise sum of given tuples.
'''
a = (1, 2, 3, 4)
b = (3, 5, 2, 1)
c = (2, 2, 3, 1)
res = []
for i in range(len(a)):
    res.append(a[i]+b[i]+c[i])
print(tuple(res))
'''

# 32. Compute Sum of All Elements of Each Tuple in a List of Tuples
# Write a Python program to compute the sum of all elements of each tuple in a list of tuples.
'''
li = [(1, 2), (2, 3), (3, 4)]
res = [sum(i) for i in li]
print(res)
'''

# 33. Convert a List of Tuples to a List of Lists
# Write a Python program to convert a list of tuples to a list of lists.
'''
li = [(100,11),(200,12)]
print(f"Original List : {li}")
li = [list(i) for i in li]
print(f"Updated List : {li}")
'''
