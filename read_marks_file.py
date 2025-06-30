file=open("Mark.txt","w")
file.write("56,57,58\n")
file.write("100,200,300\n")
file.write("96,87,78\n")
file=open("Mark.txt","r")
i=0
# now i want to read each line
while True:
    i+=1
    line = file.readline()
    if not line :
        break
    m1=line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Math:{m1}")
    print(f"Marks of student {i} in Eng:{m2}")
    print(f"Marks of student {i} in Bang:{m3}")
    print(line)