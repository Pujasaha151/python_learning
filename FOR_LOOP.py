name='babai'
for i in name:
    print(i)
print('\n')
#for list
family=["bapi",'ma','didi','ami','babai']
for k in family:
    print(k)
#for to print in range
num=int(input("Enter a number: "))
for i in range(0,num):
    print(i)

# like we want to make star
n = 5

for i in range(1, n+1 ):         # Outer loop controls rows
    for j in range( i ):     # Inner loop controls columns
        print("*", end="")        # Print stars on the same line
    print()                       # Move to the next line
print("\n")
# want
n=8
for i in range(1,n+1,2):
    for j in range(i):
        print("*",end=" ")
    print(" ")


### for loop with else
## if for successfully run then else will run..if break use then it wont run else part.
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("i am not in for loop")
print("\n")
    # can use reverse
for i in reversed(range(1, 10, 2)):
        print(i)
