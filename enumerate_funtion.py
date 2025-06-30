fruits=['banana','mango','litchi','berry']
i=0
for j in fruits:
    print(f'{i+1}:',j)
    i=i+1

#we can do that with funtion
for i,name in enumerate(fruits):
    print(i,name)
    if i==1:
        print("I love ",name)
    # we can change the start
for index, name in enumerate(fruits,start=2):
        print(index, name)
marks=[10,15,30]
for i,mark in enumerate(marks):
    print(i,".",mark)