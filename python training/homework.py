'''
For loop:
1. print numbers from 1 to 5
2.Find the maximum value in a list using for loop
3.count the number of vowels in a string using for loop
4.find and print the common elements between two lists using for loop
5.print the reverse of a string using a for loop
6.Generate a list of sequence for numbers from 1 to 10 using for loop
7.count the number of words in a sentence using for loop
8.Generate a list of prime numbers within a given range using for loop
9.calculate the sum of the first n natural numbers using for loop
10.calculate the factorial of a number using a for loop with specified step
'''
'''
While loop:
1.Basic counting:write a while loop that counts from 1 to 10 and prints each number
2.using a while loop to calculate the factorial of a given number.
3.write a while loop program that prints all even numbers between 1 to 50.
4.generate a multiplication table for given number using while loop
5.write a program using a while loop to generate the first n terms of the fibonacci sequence.
6.Build a program that checks if a given number is prime using while loop.
7.Create a program that converts a given integer into words [123 -> one hundred twenty three]
8.write a program to reverse a given string using a while loop.
9.write a program that converts a binary number to its decimal equivalent using while loop .
10.create a program that calculates and prints the prime factorization of a given number using a while loop.
'''

'''
For loop:
'''


for i  in range(1,6):
    print(i)

numbers = [10, 25, 7, 45, 18, 32]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum value:", maximum)

string = input("Enter a string:")
count=0
for char in string:
   if char in "aeiouAEIOU":
      count +=1 
print("Number of vowels:",count)

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
for item in list1:
    if item in list2:
        print(item)

string = "Thanu"
reverse = ""
for char in string:
    reverse = char + reverse
print("Reverse:", reverse)
    
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

sentence = "Python is easy to learn"
words = sentence.split()
count = 0
for word in words:
    count += 1
print("Number of words:", count)

start = 1
end = 20
primes = []
for num in range(start, end + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        primes.append(num)
print("Prime numbers:", primes)

n = 10
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum:", sum)

n = 5
factorial = 1
for i in range(1, n + 1, 1):
    factorial = factorial * i
print("Factorial:", factorial)

'''
While loop:
'''

i = 1
while i <= 10:
    print(i)
    i += 1

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("Factorial =", fact)

i = 2
while i <= 50:
    print(i)
    i += 2

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

n = int(input("Enter the number of terms: "))
a = 0
b = 1
i = 1
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1

n = int(input("Enter a number: "))
i = 2
is_prime = True
while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime and n > 1:
    print("Prime number")

def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    num_str = str(num)
    length = len(num_str)
    i = 0
    words = ""
    while i < length:
        digit = int(num_str[i])
        pos = length - i
        if pos == 3:  # hundreds place
            if digit != 0:
                words += ones[digit] + " hundred "
        elif pos == 2:  # tens place
            if digit == 1:  # handle teens
                words += teens[int(num_str[i+1])] + " "
                break
            elif digit > 1:
                words += tens[digit] + " "
        elif pos == 1:  # ones place
            if digit != 0:
                words += ones[digit] + " "
        i += 1
    return words.strip()
num = int(input("Enter a number:"))
print(number_to_words(num))

text = input("Enter a string: ")
reverse = ""
i = len(text) - 1
while i >= 0:
    reverse += text[i]
    i -= 1
print("Reversed string:", reverse)

binary = int(input("Enter a binary number: "))
decimal = 0
base = 1
while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * base
    base = base * 2
    binary = binary // 10
print("Decimal equivalent:", decimal)

n = int(input("Enter a number: "))
factor = 2
print("Prime factors:", end=" ")
while n > 1:
    while n % factor == 0:
        print(factor, end=" ")
        n = n // factor
    factor = factor + 1










































