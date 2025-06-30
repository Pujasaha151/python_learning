count=0
while (True):
    num=int(input("Enter a number (1-10):"))
    if num==0:

        break
    elif num%2!=0:
        continue
    elif num%2==0 :

        count=count+1
        print("Even number counted")

print("Total even numbers entered:",count)






