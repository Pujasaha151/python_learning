#code 1 using finally
try:
    x = 10 / 0   # Error (division by zero)
except ZeroDivisionError as z:
    print("Error occurred!",z)
finally:
    print("This runs no matter what.")
### extra
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
#code 2
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

###code 3 from video



try:
    a = int(input("enter a number :"))
    print(f"multiplication table of {a}: ")
    for i in range (1,11):
     print(f"{a}X{i}=",a*i)
except:
    print("e")
print("end")
### code 4
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
## raising error code 5
raise NameError('HiThere')
##code 6
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
### code 7
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
