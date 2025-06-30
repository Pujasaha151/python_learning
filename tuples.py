# list can change but tuples cant
# so to make a constant list we dont wabt to change
tup=(1 ,2 ,3,4,5,6)
print(type(tup))
print(tup[0])
print(tup[1:5])
#creating new tuple by slicing
tup2=tup[1:6:2]
print(tup2)
# checking the value
if 6 in tup:
    print("have 6")
else:
    print("dont have 6")

# to change the tuple we need to convert it into list then actions
family=("puja",'rita ','bapi','pinky')
print(family)
temp=list(family)
print(temp)
# now temp can change
temp.append("deba")
temp.append("joy")
print(temp)
temp.remove("joy")
print(temp)
temp.insert(3,"babai")
print(temp)
temp[0]="pomi"
print(temp)
family=tuple(temp)
print(family)
# adding 2 tuple
tup1=( 5,10,15,15)
tup2=(3,6,9,9,3,)
tup3=tup1+tup2
print(tup3)
print(tup1.count(15))
print(tup2.index(3,1,5))
'''Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple'''
country=('bd','india','china','usa','uk')
i=1
for c in country:
    print(f'{i}.',c)
    i=i+1
a=input("chose a country from this ")
if a in country:
    print(country.index(a))
else:
    print("wrong choose")



