# Python program to Print Elements in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
for ele in li:
    print(ele)
'''

# Python Program to Print List Items in Reverse Order
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
li.reverse()
print(f"Modified List : {li}")
'''

# Python Program to Print List Items Greater Than Average
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
average = sum(li) / len(li)
print(f"Average : {average} ")
for ele in li:
    if(ele > average):
        print(ele)
'''

# Python Program to Print List Items at Even Position
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
for index,value in enumerate(li):
    if(index % 2 == 0):
        print(value)
'''

# Python Program to Print List Items at Odd Position
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
for index,value in enumerate(li):
    if(index % 2 != 0):
        print(value)
'''

# Python Program to Print Even Numbers in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
for ele in li:
    if(ele % 2 == 0):
        print(ele)
'''

# Python program to Print Odd List Numbers
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
for ele in li:
    if(ele % 2 != 0):
        print(ele)
'''

# Python program to Put Even and odd Numbers in Separate List
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(f"Original List : {li}")
even = []
odd = []
for ele in li:
    if(ele % 2 == 0):
        even.append(ele)
    else:
        odd.append(ele)
print(f"Even Elements : {even}")
print(f"Odd Elements : {odd}")
'''

# Python program to Print Positive Numbers
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
for i in li:
    if(i > 0):
        print(i)
'''

# Python program to Print Negative Numbers
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
for i in li:
    if(i < 0):
        print(i)
'''

# Python program to Put Positive and Negative Numbers in Separate List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
positive,negative = [], []
for i in li:
    if(i < 0):
        negative.append(i)
    elif(i > 0):
        positive.append(i)
print(f"Positive Elements: {positive}")
print(f"Negative Elements : {negative}")
'''

# Python program to Print the Largest Number in a List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
print(f"Largest Number In List : {max(li)}")
'''

# Python program to Print the Second Largest Number in a List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
li = list(set(li))
li.sort()
print(f" Second Largest Number In List : {li[-2]}")
'''

# Python program to Print the Largest and Smallest Number
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
print(f"Smallest Number In List : {min(li)}")
print(f"Largest Number In List : {max(li)}")
'''

# Python program to Print the Smallest Element in a List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
print(f"Smallest Number In List : {min(li)}")
'''

# Python program to Remove Duplicates from List
'''
li = [1,1,2,3,4,4,2,4,5]
print(f"Original List : {li}")
li = set(li)
print(f"Modified List : {list(li)}")
'''

# Python program to Remove Even Numbers in a List
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
new_li = []
for ele in li:
    if(ele % 2 != 0):
        new_li.append(ele)
print(f"Modified List : {new_li}")
'''
    
# Python program to Reverse List Items
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
li.reverse()
print(f"Reversed List : {li}")
'''

# Python program to Sort List Items in Ascending Order
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
li.sort()
print(f"Modified List : {li}")
'''

# Python Program to Sort List Items in Descending Order
'''
li = [1,2,3,4,-5,6,7,8,9,10]
print(f"Original List : {li}")
li.sort(reverse=True)
print(f"Modified List : {li}")
'''