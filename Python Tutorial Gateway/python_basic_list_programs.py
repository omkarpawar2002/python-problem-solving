# Python Program to Append an Item to a List
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
li.append(101)
print(f"Modified List : {li}")
'''

# Python Program to access List Index and Values
'''
li = [10,20,30,40,50]
for index,values in enumerate(li):
    print(index,values)
'''

# Python Program to add two Lists
'''
li_1 = [10,20,30]
li_2 = [11,22,33]
print(li_1 + li_2)
'''

# Python Program to Change List Items
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
li[2] = 101
print(f"Modified List : {li}")
'''

# Python Program for Arithmetic Operations on Lists
'''
li_1 = [1,2,3,4,5]
li_2 = [2,2,2,2,2]
add , sub , mul , div , mod , exp , flo = [] ,[], [], [], [], [], []
for i in range(len(li_1)):
    add.append(li_1[i] + li_2[i])
    sub.append(li_1[i] - li_2[i])
    mul.append(li_1[i] * li_2[i])
    div.append(li_1[i] / li_2[i])
    mod.append(li_1[i] % li_2[i])
    exp.append(li_1[i] ** li_2[i])
    flo.append(li_1[i] // li_2[i])
print(f"Addition : {add}")
print(f"Subtraction : {sub}")
print(f"Multiplication : {mul}")
print(f"Division : {div}")
print(f"Modulus : {mod}")
print(f"Exponent : {exp}")
print(f"Floor Division : {flo}")
'''

# Python Program to Calculate the Average of List Items
'''
li = [1,2,3,4,5,6,7,8,9,10]
average = sum(li) / len(li)
print(f"Average of List Items : {average}")
'''

# Python Program to Clear a List
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
li.clear()
print(f"Modified List : {li}")
'''

# Python Program to check List is Empty or Not
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
if(li):
    print("List is not Empty")
else:
    print("List is Empty")
'''    

# Python Program to Check if the Element Exists in a List
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
print(10 in li)
print(101 in li)
'''

# Python Program to Clone or Copy a List
'''
li = [10,20,30,40,50]
print(f"Original List : {li} and Id : {id(li)}")
li_copy = li.copy()
print(f"Modified List : {li_copy} and Id : {id(li_copy)}")
'''

# Python Program to Count Occurrence of an element in a List
'''
li = [10,20,30,40,50]
print(f"Original List : {li}")
ele = int(input("Enter any input : "))
print(f"{ele} occurs {li.count(ele)} times in {li}")
'''

# Python program to Count Even and Odd Numbers in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
count_even = count_odd = 0
for i in li:
    if(i % 2 == 0):
        count_even += 1
    else:
        count_odd += 1
print(f"Total Even Count : {count_even}")
print(f"Total Odd Count : {count_odd}")
'''

# Python program to Count Positive and Negative Numbers in a List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
positive = negative = 0
for i in li:
    if(i < 0):
        negative += 1
    elif(i > 0):
        positive += 1
print(f"Total Positive Count : {positive}")
print(f"Total Negative Count : {negative}")
'''

# Python program to find Length of a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Length of List : {len(li)}")
'''

# Python program to find the List Difference
'''
li_1 = [1, 2, 4, 6, 8, 9]
li_2 = [1, 3, 5, 7, 11, 9]
s1 = set(li_1)
s2 = set(li_2)
s1_diff = s1.difference(s2)
s2_diff = s2.difference(s1)
li_1 = list(s1_diff)
li_2 = list(s2_diff)
print(li_1 + li_2)
'''

# Python Program to Find the Average of a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
average = sum(li) / len(li)
print(f"Average of list items : {average}")
'''

# Python Program to Merge Two Lists
'''
li_1 = [10,20,30,40,50]
li_2 = [11,22,33]
print(f"List 1 are : {li_1}")
print(f"List 2 are : {li_2}")
li_1.extend(li_2)
print(f"After Merging  : {li_1}")
'''

# Python List Multiplication Program
'''
li = [1,2,3,4,5]
product = 1
for i in li:
    product = product * i
print(f"Multiplication of all list elements : {product}")
'''

# Python program to find the Sum of All List Elements
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Sum of all list elements are : {sum(li)}")
'''

# Sum and Average of a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
total = sum(li)
average = total / len(li)
print(f"Sum of list are {total} \nAverage of list are {average}")
'''

# Sum of Even and Odd List Numbers
'''
li = [1,2,3,4,5,6,7,8,9,10]
sum_of_even = sum_of_odd = 0
for i in li:
    if(i % 2 == 0):
        sum_of_even += i
    else:
        sum_of_odd += i
print(f"Sum of even number : {sum_of_even}")
print(f"Sum of odd number : {sum_of_odd}")
'''

# Left Rotate a List by n
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
num = int(input("Enter how many elements rotate to left : "))
for i in range(num):
    ele = li.pop(0)
    li.append(ele)
print(f"Modified List : {li}")
'''

# Right Rotate a List by n
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
num = int(input("Enter how many elements rotate to right : "))
for i in range(num):
    ele = li.pop()
    li.insert(0,ele)
print(f"Modified List : {li}")
'''

# Remove an item from a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li.remove(4)
print(f"Modified List : {li}")
'''

# Remove the First element from a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li.pop(0)
print(f"Modified List : {li}")
'''

# Remove the Last Element from a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li.pop()
print(f"Modified List : {li}")
'''

# Iterate Over List Items
'''
li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    print(i)
'''

# Interchange First and Last Elements in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li[0] , li[-1] = li[-1] , li[0]
print(f"Modified List : {li}")
'''

# Swap two items in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li[2],li[3] = li[3],li[2]
print(f"Modified List : {li}")
'''