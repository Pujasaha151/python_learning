#write a program where it asks you  to enter a user name then a list of defined topic e.g. age, sex, height etc. and specific info e.g. 25, female, 5.7 etc. for that particular user entry, it will ask you indefinitely until you say you dont want to enter any new user info (it will also ask as many new info for the user you want to enter), you have to use a dictionary here, and then after entering all the whatever info you want to store for the number of users of your choice, then input a specific user name and what info you want to know about them, it will print that speicifc info with that user name e.g. Joy, dick size:
#6 inches or Puja, joy's favorite: boobies etc.'''
fin_dick = {}

while True:
    query = input("you want  add more Users:")
    if query=="yes":
        name=input("Enter user name:")
        dic = {}
    else:
        break

    while query:
        q =input("you want to add more info:")
        if q=="yes":
            key = input("which info u want to give")
            value = input("ans")
            dic[key] = value
            continue
        else:
            break
    fin_dick[name]=dic
print(fin_dick)
while True:
 x=input("if you want to ask more about someone keep asking")
 if x=="ok":
  p=input("whom info u want to know:")
  info={}
  info=fin_dick[p]
  key=input("which info u want to know?")
  print(f"{p}, {key}: {info[key]}")
 else:
   break
