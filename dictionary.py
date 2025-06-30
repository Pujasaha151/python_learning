dic={'name':'puja','age':23,'dept':'cse'}
print(type(dic))
print(dic.keys())
print(dic.values())
print(dic['name'])
# if dont have key it will not give error
print(dic.get('puja'))
# using loop to show key
for i in dic:
    print(i)

# using loop to show vaule
for j in dic.keys():
    print(dic[j])
# to get key value pair we can use item
print(dic.items())
for key,val in dic.items():
    print(key,val)
#oparetions
tel = {'jack': 4098, 'sape': 4139}
# adding
tel['puja']=5044
print(tel)
list(tel)
print(tel)
p={x: x**2 for x in (2, 4, 6)}
print(p)
dic.clear()
print(dic)
