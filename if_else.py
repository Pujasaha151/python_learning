from base64 import b32decode
from turtledemo.sorting_animate import enable_keys

num=int(input('take a number: '))
if num==0:
    print('the number is zero')
elif(num>0 and num!=20):
    print('the number is positive')
elif(num==20 ):
    print('the number is special')
else:
    print('the number is negative')
# shorthand if else statement
a=2
b=3
print("a") if a>b else print("=") if a==b else print("b")

c=9 if a>b else ''
# or if a>b else 0
print(c)
