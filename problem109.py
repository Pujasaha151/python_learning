print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item too the file")
n=int(input("Make a selection 1,2 or 3 : "))
if n>3 or n<0:
    raise ValueError("Invalid input")


if n==1:
        sub=input("Enter a school subject:")
        file=open("Subjects.txt","w")
        file.write(sub + "\n")
        file.close()
elif n==2:
    file = open("Subjects.txt", "r")
    print(file.read())
    file.close()
else:
      sub1 = input("\nEnter a  new school subject:")
      file = open("Subjects.txt", "a")
      file.write(sub1 + "\n")
      file.close()

