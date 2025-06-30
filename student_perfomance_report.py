heading="\033[1m" '--Student Performance Report Generator--'"\033[0m"
print(heading.center(80))
print("."*80)
print("1) Add Student")
print("2) View All Reports")
print("3) Search by Name")
print("4) Exit\n")
print("Enter your choice from 1 to 4")
a=int(input("enter choice:"))
if a == 1:
    name = input("Enter student name: ")
    for i in range(0,3):
       int(input(f"Enter mark {i+1}:"))
print("Student",name,"added successfully!")


