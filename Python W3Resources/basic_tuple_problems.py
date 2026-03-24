# Python Tuple Exercises (1–33)

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



# 18. Reverse a Tuple
# Write a Python program to reverse a tuple.

# 19. Convert a List of Tuples into a Dictionary
# Write a Python program to convert a list of tuples into a dictionary.

# 20. Print Tuple with String Formatting
# Write a Python program to print a tuple with string formatting.

# 21. Replace the Last Value of Tuples in a List
# Write a Python program to replace the last value of tuples in a list.

# 22. Remove Empty Tuple(s) from a List of Tuples
# Write a Python program to remove empty tuple(s) from a list of tuples.

# 23. Sort a Tuple by Its Float Element
# Write a Python program to sort a tuple by its float element.

# 24. Count Elements in a List Until an Element is a Tuple
# Write a Python program to count the elements in a list until an element is a tuple.

# 25. Convert a Given String List to a Tuple
# Write a Python program to convert a given string list to a tuple.

# 26. Calculate the Product of Numbers in a Tuple
# Write a Python program to calculate the product of numbers in a tuple.

# 27. Calculate Average Value of Numbers in a Tuple of Tuples
# Write a Python program to calculate the average value of numbers in a tuple of tuples.

# 28. Convert a Tuple of String Values to a Tuple of Integer Values
# Write a Python program to convert a tuple of string values to a tuple of integer values.

# 29. Convert a Tuple of Positive Integers into an Integer
# Write a Python program to convert a tuple of positive integers into an integer.

# 30. Check if a Specified Element Appears in a Tuple of Tuples
# Write a Python program to check if a specified element appears in a tuple of tuples.

# 31. Compute Element-wise Sum of Given Tuples
# Write a Python program to compute the element-wise sum of given tuples.

# 32. Compute Sum of All Elements of Each Tuple in a List of Tuples
# Write a Python program to compute the sum of all elements of each tuple in a list of tuples.

# 33. Convert a List of Tuples to a List of Lists
# Write a Python program to convert a list of tuples to a list of lists.