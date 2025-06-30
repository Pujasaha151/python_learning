name=input('Enter username: ')
password=int(input('Enter password: '))
if(name=="puja" and password==1234):
    print("Login successful!")
else:
    print("Invalid username or password!")
## new problem

check=input("Give a meaningful sentence: ")
if(check.isspace()):
    print("Empty input!")
else:
    print(len(check))
    print(check.isupper())
    print(check.isprintable())
    print(check.endswith('.'))
print('ends')
