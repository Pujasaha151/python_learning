# to get the cube of each item in list
cube=lambda x:x**3
l=[1,2,3,4,5,6,7]
print(l)
new=[]
for item in l:
    new.append(cube(item))
print(new)
print("using map")
## using map()
newl=list(map(cube,l))
print(newl)
### Filter funtion .which only works with function that True or false
def x(a):
    return a==4
a=int(input(" give a num:"))
print(x(a))
filter_fun=list(filter(x,l))
print(filter_fun)
### reduce()
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24

reduce(lambda x, y: x + y, ["Puja", " is", " awesome!"])  # ➡️ 'Puja is awesome!'
reduce(lambda x, y: x if x < y else y, [4, 8, 2, 6])  # ➡️ 2
