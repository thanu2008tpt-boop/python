# t=(10,)#remove camma when string and noo string we get int, str 
# print(t)
# print(type(t))


# #Indexing
# t2=(10,20,30,'python',True)
# print(t2[1])
# print(t2[2])
# 


# #slicing
# print(t2[::-1])
#print(t2[0:4])

#Sorted->ascending order nunchii start avuthundhii 
# t5=(40,50,10,20,100)
# t6=(tuple(sorted(t5)))
# print(t6)



# t4=('python','reactjs','swift')
# print(min(t4))
# print(max(t4))


# T=(10,20,30,30,20,30,20,30,20,30,40,20,30)
# print(len(T))
# print(T.count(20))
# print(T.index(10))
# min(T)
# print(min(T))
# max(T)
# print(max(T))

#concatenation
# x=(10,20,30)
# y=(20,30,40)
# print(x+y)

# #repetition
# x=(10,20,30)
# y=3
# print(x*y)

# #membership
# x=(3,6,9,12,15)
# print(6 in x)
# print(4 in x)

def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
#f(3,2) # 3,2,4,8-> positional with default 
#f(10,20,30,40) #10,20,30,40 ->Positional arg 
#f(25,50,arg4=100)  #25,50,4,100->positional with default 
#f(arg4=2,arg1=3,arg2=4)#3,4,4,2 ->keyword arg
#f()#Error
#f(4,5,arg2=6)#Error
#f(arg3=10,arg4=20,30,40)#Error
#f(4,5,arg3=5,arg5=6)#Error