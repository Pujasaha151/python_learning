# def sumation(a):
#   ''''this is doc string which we can see and must write'''
#   s=0
#   for i in range(1,a+1):
#     s = s + i
#   print("the value of the series :",s)
# n=int(input("enter the number u want to sum from 1:"))
# sumation(n)
# print(sumation.__doc__)
# ###code 2
# def suq(b):
#    print( b**2)
#
# n=int(input("enter the number u want to squre :"))
# suq(n)

###code 3 where we can pass a fuction by a funtion
def fun2(f,p):
  x= 6+f(p)
  print(x)

def fun1(value):
  y=value**3
  return y

#n=int(input("ENTER THE VALUE:"))
fun2(fun1,2)
### lamda funtion
double=lambda x: x*2
cube=lambda y:y**3
avg=lambda p,q,r:(p+q+r)/3
n=int(input("ENTER THE VALUE:"))
print(double(n))
fun2(cube,2)
mul_line=lambda x,y:print(f"the multiplication of {x}X{y} is :{x*y}")
