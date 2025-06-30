# votting problem
def vote(age):
    if age<18:
        raise ValueError("u are small")
    else:
        print("you are capable of voting")
try:
 age1=int(input("enter your age:"))
 vote(age1)
except ValueError as error:
     print(error)

## baler quit problem ta
a=input("fx")
if a=='quit':
    print("dont")
elif int(a)>5 or int(a)>9:
    raise ValueError("vdxu")
else:
    print("gxud")
