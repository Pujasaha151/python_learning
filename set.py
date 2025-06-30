
# set is a collection of well defined  object that doesnt  repeat value and unordered
s={1,2,2,2,3,4,6}

print(s)
info={"puja",23,False,5.8,23}
print(info)
# to make empty set
harry=set()
print(type(harry))
# to access the value
for value in info:
    print(value)

# joining sets
# union
s1={1,2,3,4,5}
s2={3,7,9}
s3=s1.union(s2)
print(s3)
print(s1,s2)
# updating
s1.update(s2)
print(s1,s2)
#intersection
s4=s1.intersection(s2)
print(s4)
s1.intersection_update(s2)
print(s1,s2)
# symetric diff means a union b theke a intersection mane common jinish bad
c={'a',"b","c",'c'}
b={"b","c","y",'x'}
d=c.symmetric_difference(b)
print(d)
# difference
e=c.difference(b)
print(e)
b.difference_update(c)
print(c,b)
#method or funtions isdisjoint,issuperset,add
cse={"data","ml","dl","image"}
eee={'circuit','ware','current'}
ete={'data',"ml","dl"}
print(cse.isdisjoint(eee))
print(cse.issuperset(ete))
print(ete.issubset(cse))

cse.add("mining")
print(cse)
ete.remove("dl")# cann't handle error
eee.discard("ware")
print(ete, eee)
x=cse.pop()
print(cse)
# showing which one will pop last but it will random
print(x)
ete.clear()
print(ete)
# it will delete cse
del cse
