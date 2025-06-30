# here x is global we can access it from fuction but its value wont change
x=4
def local():
    '''Dic string'''
    y=10
    print(y)
    x=20
    print(x)
    print("hi am from funtion local")
local()
print(x)
print(local.__doc__)
print(" to watch gobal variable change")
# but if i want to change global variable from funtion i need to use gobal
x=5
def local():
    '''Dic string'''
    y=10
    print(y)
    global x
    x=20
    print(x)
    print("hi am from funtion local")
local()
print(x)