'''
'---------------------------------------------------STRINGS--------------------------------------------------'
1.write a python program to reverse a string.
2.write a program to print characters at odd positions and even positions for the given string.
3.write a program to check the character exists in the given or not.
4.write a python program to count vowels in the string.
5.write a python program to print first and last character of given string.
6.write a python program to remove all vowels from a given string.
7.write a python program a string by replacing each letter with other letter.
8.write a python program if two given strings are anagrams.
9.write a program to perform basic string compression using count of repeated characters.
10.write a program to perform remove duplicates from the given string.

'---------------------------------------------------LISTS------------------------------------------------------'
1.reverse a list
2.remove duplicates from a list
3.find the max and min of a list 
4.sort a list in asc and desc order
5.check if a list is empty or not 
6.find the index of specific element in a list
7.merge two list in python
8.find the sum of all elements in a list 
9.slice a list to get specific element
10.find the second largest element in the list 
11.find the common elements in 2 lists

'----------------------------------------------------TUPLE-------------------------------------------------------'
1.find the first and last occurance of a specific element in tuple
2.2.1 Reverse a tuple
  2.2 concatenate two tuples
3.3.1 Find the max and min elements in tuple
  3.2 sort a tuple of numbers in ascending order
4.4.1 check the tuple contains unique elements
  4.2 Multiply a tuple to repeat its elements
  4.3 unpack a tuple into individual variables
5.5.1 find the differences between 2 tuples
  5.2 combine multiple tuples into one tuple 
  5.3 find even numbers by using exisiting tuple
6.check if a tuple contains only numeric elements
7.find the sum of all elements in a tuple
8.find the tuple max sum in a tuple

'----------------------------------------------------SET-----------------------------------------------------------'
1.create a empty set in python and add or remove an  element to a set
2.check if a set is empty without usinng len()
3.Update the set of elements from another set
4.find the sum and average of all elements in a set
5.find the most common element in a set
6.check if a set is a super set of multiple from a list

'----------------------------------------------------DICTIONARY----------------------------------------------------'
1.create a dictionary containing a students name,age,course and marks.
print all the keys and values.
2.Dictionary Operators
  create a student dictionary of 5 products and their prices
  check whether a given product exists using the 'in' operator and display its price if available.
3.Add and Update
  create a student dictionary .Take a new value from the user and add a new key-value pair.
  Then update the student's marks.
4.create a dictionary containing student names and marks.Use 'if-else to print whether each student has passed or failed
5.create a dictionary containing subjects and marks .Use a for loop to calculate the total and average marks.
6.create a dictionary containing 5 numbers.Use a for loop and if-else to identify whether each value is even or odd.
7.create a dictionary containing names and student marks .Using a for loop and if condition,
   find the student with the highest marks without using max()
8.create a dictionary containing IDs and names .Use a while loop to repeatedly ask for a student ID  and display the student's names.
   stop when the user enters "stop"
9.create a dictionary containing products and prices.Use a for loop and break to search for a product and stop the loop when the product is found
10.create a dictionary containing product and stock quantities .Use for and continue to skip products whose stock is '0' and print only available products
11.create a dictionary containing product names and prices.
  Ask the user to enter products one by one using a while loop.
  Use if-else to check availability,continue for invalid products and break when the user enters checkout.
  calculate the final bill
'''

'String'

# s = "Java is Programming language"
# print(s[::-1])

# s = input("Enter a string: ")
# print("Even position characters:")
# print(s[::2])
# print("Odd position characters:")
# print(s[1::2])

# s = input("Enter a string: ")
# ch = input("Enter a character: ")
# if ch in s:
#     print("Character exists")
# else:
#     print("Character does not exist")

# s = input("Enter a string: ")
# count = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count += 1
# print("Number of vowels:", count)   

# s = input("Enter a string: ")
# print("First character:", s[0])
# print("Last character:", s[-1])

# s = input("Enter a string: ")
# for ch in s:
#     if ch not in "aeiouAEIOU":
#         print(ch, end="")

# x='poojitha'
# print  (x.replace("poojitha",'qppkjuib'))

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# s = input("Enter a string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if i < len(s) - 1 and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# print("Compressed string:", result) 

# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print("After removing duplicates:", result)

'List'

# x=['python','java','reactjs']
# print(x[::-1])

# a = [1, 2, 2, 3, 4, 4, 5]
# b = list(set(a))
# print(b)

# x=[10,30,50,70]
# min(x)
# print(min(x))
# max(x)
# print(max(x))

# m=[64,8,42,88,13]
# n=[list(sorted(m))]
# print(n)
# n=sorted(m,reverse=true)
# print(n)

# a = []
# if not a:
#     print("List is empty")
# else:
#     print("List is not empty")

# x=[10,20,30,40]
# print(x.index(30))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# a = [1, 2, 3, 4, 5]
# sum = 0
# for i in a:
#     sum += i
# print("Sum =", sum)

# x=[10,20,30,'python','java']
# print(x[1:4])

# a = [10, 20, 5, 30, 15]
# largest = max(a)
# a.remove(largest)
# second = max(a)
# print("Second largest:", second)

# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8,9,10,11}
# print(s1.intersection(s2))

'Tuple'

# a = (10, 20, 30, 20, 40, 20)
# x = 20
# print("First occurrence:", a.index(x))
# print("Last occurrence:", len(a) - 1 - a[::-1].index(x))

# x=(10,20,30)
# y=(20,30,40)
# print(x+y)
# x=(10,20,30,40,50)
# print(x[::-1])

# k=('bhavya','yamini','rithya')
# print(min(k))
# print(max(k))
# a = (5, 2, 8, 1, 3)
# b = sorted(a)
# print(b)

# a = (1, 2, 3, 4, 5)
# if len(a) == len(set(a)):
#     print("All elements are unique")
# else:
#     print("Duplicate elements are present")
# a = (1, 2, 3)
# b = a * 3
# print(b)

# s1={1,2,3,4,5}
# s2={3,4,5,6,7}
# print(s1.difference(s2))
# a = (1, 2)
# b = (3, 4)
# c = (5, 6)
# d = a + b + c
# print(d)
# a = (1, 2, 3, 4, 5, 6)
# for i in a:
#     if i % 2 == 0:
#         print(i)

# a = (10, 20, 30, 40)
# if all(isinstance(i, (int, float)) for i in a):
#     print("Tuple contains only numeric elements")
# else:
#     print("Tuple contains non-numeric elements")

#     a = (10, 20, 30, 40)
# print("Sum =", sum(a))

# a = (10, 20, 30, 40)
# print("Maximum element:", max(a))
# print("Sum of elements:", sum(a))

'set'

# a = set()
# a.add(10)
# print(a)
# a.remove(10)
# print(a)

# a = set()
# if not a:
#     print("Set is empty")
# else:
#     print("Set is not empty")

# a = {1, 2, 3}
# b = {4, 5, 6}
# a.update(b)
# print(a)

# a = {10, 20, 30, 40}
# total = sum(a)
# average = total / len(a)
# print("Sum =", total)
# print("Average =", average)

# a = [1, 2, 2, 3, 2, 4]
# print(max(set(a), key=a.count))

# a = {1, 2, 3, 4, 5}
# b = [2, 3, 4]
# if a.issuperset(b):
#     print("It is a superset")
# else:
#     print("It is not a superset")

'Dict'

student = {
    "name": "Thanu",
    "age": 18,
    "course": "Python",
    "marks": 90
}
for key, value in student.items():
    print(key, ":", value)

products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}
product = input("Enter product name: ")
if product in products:
    print("Price:", products[product])
else:
    print("Product not available") 

student = {
    "name": "Thanu",
    "age": 18,
    "marks": 80
}
key = input("Enter new key: ")
value = input("Enter value: ")
student[key] = value
student["marks"] = 90
print(student)  

students = {
    "rani": 80,
    "Raju": 35,
    "Vamsi": 60
}
for name, marks in students.items():
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name, "Failed")

student = {
    "Maths": 80,
    "Science": 70,
    "English": 90
}

total = 0
for marks in student.values():
    total += marks
average = total / len(student)
print("Total marks:", total)
print("Average marks:", average)

numbers = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 25,
    "e": 30
}
for value in numbers.values():
    if value % 2 == 0:
        print(value, "Even")
    else:
        print(value, "Odd")

students = {
    "Tejusree": 85,
    "Rithyasree": 92,
    "pujasree": 78,
    "Thanmayi sree": 88
}
highest = 0
name = ""
for student, marks in students.items():
    if marks > highest:
        highest = marks
        name = student
print("Student with highest marks:", name)
print("Highest marks:", highest)  

students = {
    101: "Mahi",
    102: "keeru",
    103: "neha",
    104: "jashuu"
}
while True:
    id = input("Enter student ID: ")
    if id == "stop":
        break
    id = int(id)
    if id in students:
        print("Student name:", students[id])
    else:
        print("Student not found")

products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 100
}
search = input("Enter product name: ")
for product, price in products.items():
    if product == search:
        print("Price:", price)
        break
else:
    print("Product not found")

products = {
    "Pen": 10,
    "Book": 0,
    "Bag": 5,
    "Bottle": 0,
    "Pencil": 20
}
for product, stock in products.items():
    if stock == 0:
        continue
    print(product, ":", stock)

products = {
    "apple": 50,
    "milk": 30,
    "bread": 40,
    "rice": 60,
    "sugar": 45
}
total = 0
while True:
    product = input("Enter product (or checkout): ").lower()
    if product == "checkout":
        break
    if product not in products:
        print("Product not available")
        continue
    price = products[product]
    total = total + price
    print(product, "added - ₹", price)
print("Final Bill = ₹", total)