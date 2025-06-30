'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#5 * factorial(4)
# 5*4*factorial(3)
## fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:

         return  fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''

#Write a recursive function to sum all the digits of a number.


def sumofdigit(n):
  if n==0:
      return 0
  else:
   x=n%10
   y=n//10
   return x+sumofdigit(y)
p=int(input("Enter a number:"))
print(sumofdigit(p))
