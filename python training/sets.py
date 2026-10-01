# s={}
# print(s)
# print(type(s))

# s={1,2,3,4,5}
# print(type(s))
# print(s[2])
# print(s[1:5])

# l=[1,2,3,4,5]
# s=set(l)
# print(s)

s1={1,2,3,4,5}
s2={6,7,8,9,10}
print(s1.union(s2))
print(s1|s2)

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
print(s1.intersection(s2))

s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.difference(s2))
print(s2.difference(s1))

s={1,20,32,46,50,60,78,34}
print(s)