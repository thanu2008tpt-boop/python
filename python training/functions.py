'''
--------------------------------------Functions----------------------------------
*Function is a group of statement repeteadly required.soo we not recomand to write this statement separately.
*So we have too define this statements as a single unit and we can call that unit any number of types based on our requirement without rewritting.
*Function is a block of code designed to perform a specific task.
*Funtions are two types.They are
 1.Pre-defined functions or Built -in functions
 2.User-defined functions
*Pre-defined functions or Built-in functions:
                This functionss are coming along with python software automatically are called as Pre-defined functions.
             ex:print(),type(),input(),output(),id().............etc.
*User-defined functions:
                The functions which are developed by the programmers explictly according to their business requirement are called as User-defined functions. 
*syntax     Function creation
   def function-name():
      statement
   function-name()                          
'''

#parameters 
# def sum(a,b,c):
#     result=a+b+c
#     print("The sum of 3 numbers:",result)

# sum (10,20,30)#Valid
# # sum(10)#Invalid
# # sum(10,20,30,40)#Invalid

# def area(r):
#     result=22/7
#     area=result*r*r
#     print(area)    
# area(7)

# def square_number(x):                           #def square_it(number):
#     square_number=x*x                               result = number*number
#     print(square_number)                            print(result)
#square_number(6)                                  square_it(5) 

# def shopping_bill(price,quantity):              
#     result = price*quantity
#     print("The total bill is :",result)
# shopping_bill(20,30)   

# #write a function for that give number even or not.
# def check_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Not Even"
# n = int(input("Enter a number: "))
# print(check_even(n))

'''
Return statement:Functions can take input as parameter and execute business logic and return output with the return statement.
''' 
# 'example:'
# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result)   

# def mul(a,b):      
#     return a*b          
# print(mul(3,4))

# def mul(a,b):
#     return a*b
# result=mul(3,4)
# print(result)
   
'''
--->Types of arguments:
    ------------------

1.Positional args:
------------------
   *These are the Arguments passed to function in correct positional order.
   *The no.of args and position of args must be matched .
      If we change the order then the result will changed .
      If we change the no.of args then we will get an error.

2.Keyword args:
---------------
   *We can pass argument values by keyword i.e parameter name 
   *Here the order of args is not important but number of args must be matched 

Note:
-----
*We can use both positional and keyword argument simultaneosly.
But first we have to take positional arguments then keyword args,
otherwise we will get error

3.Default args:
--------------
*Sometimes we can provide default values for our positional args.
*If we are not passing any name then only default value will be considered.

4.Variable-length args:
----------------------
*Sometimes we can pass any no.of args to our function,
such type of args are called as variable-length of args.
*We can declare a variable length args with *symbol as:
      def f1(*n):
*We can call this function by passing any no.of args including zero,
 internally all these values represented in the tuple.
*After variable length arg,if we are taking any other args then we should provide values as keyword args.       

***Positional args:
            def sum(a,b)
              result=a+b
              print(result)
            sum(5,3)

***Keyword args:
              def greet(name,wish)
                 print('Hello',name,wish)
              greet(name='Thanu',wish='good morning')
'''

'------------------------------Positional args----------------------------------'
# def greet(name,wish):
#     print("Hello",name,wish)
# greet('Thanu','good morning') 

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     result=sum,sub
#     print(result)
# sum_sub(100,500)
# sum_sub(500,100)
'-------------------------------Keyword args------------------------------------'
# def greet(name,wish):
#     print("Hello",name,wish)
# greet(name="Thanu",wish='Good afternoon')  
# greet(wish='Good afternoon',name="Thanu") 
# #greet(name="Thanu",'good afternoon')#Invalid

# def greet(name,age,city):
#     print(name,age,city)
# greet(name="Thanu",age='18',city='Tirupathi')  

# def greet(name,place,college):
#     print(name,place,college)
# greet(name="Thanu",place="gajulamandyam",college="MRDU")    

'-------------------------------Default args--------------------------------------'
# def greet(name='Thanu',age=25):
#      print("Hello",name,age)
# greet()

# def movie(hero='NTR'):
#     print('Hi',hero)
# movie()
# movie('Pawan kalyan')    

'--------------------------------Variable-length------------------------------------'
# def f1(*a):                #def f1(*a): #single parameters pass chesii multiple arguments isthundhi then the output becomes tuple
#     print(a)               # print(*a)
#     print(type(a))         #  print(type(a))
# f1(10,20,30)               #f1(10,20,30)

# def f2(n1,*s):
#     print(n1)
#     print(*s)
# f2(10,'A',20,'B',30,'C')    

# def f3 (*s,n2):
#     print(s)
#     print(n2)
# f3(10,'A',20,'B',30,n2='C')    
'''
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,2) # 3,2,4,8-> positional with default 
f(10,20,30,40) #10,20,30,40 ->Positional arg 
f(25,50,arg4=100)  #25,50,4,100->positional with default 
f(arg4=2,arg1=3,arg2=4)#3,4,4,2 ->keyword arg
f()#Error
f(4,5,arg2=6)#Error
f(arg3=10,arg4=20,30,40)#Error
f(4,5,arg3=5,arg5=6)#Type Error
'''
# def f1(**a):
#     print(a)
#     print(type(a)) 
# f1(a=10,b=20,c=30,d=40) 

'''
Function:A group of line with some name is called function.
A group of functions saved in one file is called module.
A group of modules is ntg but a package.
A group of package is ntg but a library.

In Python There are two variables :
Types Of Variables
------------------
1.Global Variable
2.Local Variable

1.Global Variable:
-----------------
 *If the value of a variable is defined out side a function such type of variable is called Global Variable.
   This variable can be access inside and outside of the function

Variable_name=value:
'''
# a='This is Global Variable'
# b=10
# def g():
#     print(a)
#     print(b)
# def g1 ():
#     print(a)
#     print(b)
# g()
# g1()  
'''
2.Local Variable:
----------------
 *The variables which are declared inside a function are called Local variables.
LOcal variables are available only for the in which function declared that is outside of the variable we Can't access
'''
# def l():
#     a='This is Local'
#     b=10
#     print(a)
#     print(b)
# def l1():
#     print(a)
#     print(b)  
# l()
# l1()

# a='This is global variable'
# b=10
# #Creating function
# def g():
#     print(a)
#     print(b)
# #Creating another function    
# def g1():    
#      print(a)
#      print(b)
# #Calling function     
# g()
# g1()    

# def m():
#      x='This is Local variable'
#      y=20
#      print(x)
#      print(y)
# #Creating another function

# def m1():
#      print(x)
#      print(y) 
# #Calling function     
# m()
# m1()     

'''
Lambda Functions Or Anonymous Functions:
---------------------------------------
*Sometimes we can declare a function without name,such type of nameless functions are called as anonymous functions or lambda expressions. 
*The main advantage of ananymous function is just for instant use
(i.e for one time usage)

Syntax:-
     lambda arguments_list :expression

Note:
    By using lambda functions we can write concise code so that readability of the program will be  improved.

Note:
    Lambda function internally returns expression value and we are not required to write return statement explicitly. 

sometimes we can pass function as argument to another function.
In such case lambda functions are best choice.

We can use lambda functions very commonly with filter(),map() and reduce()
functions because these functions expect function as argument.
'''

'''
# Normal function:
# ---------------
def squareit(n):
     return n*n
print(squareit(3))
print(squareit(4))    

# Lambda function:
-----------------
s=lambda n:n*n
print('The square of 3 is:',s(3))
print('The square of 5 is:',s(5))
'''

# #Normal function
# def square(n):
#  return n*n
# result=square(5)
# print(result)

# s=lambda n:n*n
# print(s(5))

# s=lambda n:n+n
# print(s(3))

# s=lambda m:m%2==0
# print(s(2))
# print(s(5))

# s=lambda m,n:m>n 
# print(s(20,10))

'''
# Recursive function :
---------------------
*calling a function itself is called recursive function .'''

#Normal function 
# def factorial(n):
#     result=1
#     while n>=1:
#         result=result*n 
#         n=n-1
#     return result
# print(factorial(5)) 

# #Recursive function 
# def fact(n): 
#     if n ==0:
#         return 1
#     else:
#         result= n*fact(n-1)
#     return result    
# print(fact(5))

def palindrome(string):
    if string =="Racecar":
        return "Racecar"
    else:
        result=string*"Racecar"
    return result
print(palindrome()) 




#string = input("enter a string:")
#if string==string[::-1]:
#print("the given string is palindrome")
#else:
#print("the given string is not a palindrome"