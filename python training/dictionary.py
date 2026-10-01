s={}
print()
print(type(s))

#creating dict
d1 = dict({100:'avinash',200:'srikhar',300:'kiran'})
print(d1)
d2 = dict([(333,'mohit'),(666,'sai charan'),(999,'abhi')])
print(d2)
d3 = dict((('l','ravi'),('r','uday'),('s','sunny')))
print(d3)

#len
d1 = dict({100:'mohit',200:'sai charan',300:'abhi'})
print(len(d1))

#clear
d1 = dict({100:'mohit',200:'sai charan',300:'abhi'})
print(d1.clear())

#get
d1 = dict({100:'mohit',200:'bunny',300:'abhi'})
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d[100])
print(d[400])#key error
print(d.get(100))
print(d.get(400))#none
print(d.get(100,'mohit'))
print(d.get(400,'mohit'))

#pop
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.pop(300))
print(d.pop(400))#key error

#pop item 
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.popitem())

d={}
print(d.popitem())#key error

#keys
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.keys)
for k in d.keys():
    print(k)

#values 
d = {100:'mohit',200:'bunny',300:'abhi'}    
print(d.values())
for k in d.values():
    print(k)

d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.items())
for k,v in d.items():
    print(k,'--->',v)

#copy
d = {100:'mohit',200:'bunny',300:'abhi'}
d1= d.copy()
print(id(d))
print(id(d1))

#set default
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.setdefault(100,'mohit'))
print(d.setdefault(400,'vamsi'))
print(d)

#update
d = {100:'mohit',200:'bunny',300:'abhi'}
d1 = {'a','apple'}
d.update(d1)
print(d)
d.update([(333,'A')])
print(d)