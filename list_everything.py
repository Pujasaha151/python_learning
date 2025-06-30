marks=[1,2,3,4]
print(marks)
print(type(marks))
a=[1,2,3,"puja",True]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[:])
print(a[1:3])# 3 excluded just 1,2

name=["puja" ,"joy","pinky","rita","anup","vai"]
print(name[0:4:2])
print(name[1::2])
# check if  any value is there or not
if 'puja' in name:
    print("---Yes it has puja--")
# list comprehension
#for loop if else

listt=[ i for i in range(11)]
print(listt)
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print(S)
# Q = {$x^3$: x in {0 ... 10}}
Q=[x**3 for x in range(11)]
print(Q)
Q=[x**3 for x in range(11) if x%2==0]
print(Q)
# operations or method in list


l=[12,11,15,1,4,3,5,7,10,1,2,3,4]
#to change
l[0]=20
print(l)
print(len(l))
l.sort()
print(l)
l.sort(reverse=True)# decending order
print(l)
l.append(100)
print(l)
# or we can add value through inteet with index
l.insert(2,505)
print(l)
# to remove single value
l.remove((20))


l.reverse()# reverse the list
print(l)
print(l.index(3))
print()
print(l.count(3))
# we can copy a list
m=l.copy()
print("this a copy list",m)
# we can sum 2 or more list
m=["puja ", "Pinky"]
k=m+l
print(k)
# we a add a list by extand
l.extend(m)
print("this means m add to l ",l)
# to remove multiple value
marks = [80, 90, 100, 80, 90, 100]
marks = [x for x in marks if x not in [80, 90]]
print(marks)
# to zip to list
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))