from itertools import repeat

name="puja"
age="23"
Dept="cse"
print("hello I am " +name+" My age is",age,'currently reading in Dept',Dept)
print(name[3])
apple='''hgucdeiubd
dugcujehkchjdvcj
cdgdjched'''
print('lets use a for loop to print char each')
for i in apple:
    print(i)
### string slicing
name='puja,joy,pinky,babai,rita,anup '
print(len(name))
print(name[0:3])
print(name[4:9])
print(name[:4])
print(name[0:])
print(name[:-4])
print(name[-5:])
print(name[1::2])
print(name[:6:3])# last 3 means 2 step will skip
# hoe to reverse
s = "hello"
rev = s[::-1]
print(rev)  # Output: "olleh"
# adding
s1 = "Hello"
s2 = "World"
result = s1 + s2
print(result)  # Output: HelloWorld
# add something
# add something
s="python"
s += "3"           # "pytho3"



#diff function for string operation
a='puja is A good girl'
print(a.upper())
a='PUJA is A GOOD GIRL.'
print(a.lower())
b="!PUJA IS A GOOD GIRL!!!"
print(b.swapcase())
print(b.rstrip("!"))
c="!!!PUJA IS A GOOD GIRL    "
print(len(c))
print(len(c.rstrip(" ")))
#seeing what happend after and before
d="puja is a girl!!  \n "
print(repr(d))            # Before rstrip
print(repr(d.rstrip()))
#remove from left side
e="!!!PUJA IS leaeing python     "
print(e.lstrip('!'))
#removing from both
print(b.strip('!'))
#Capitalize make 1st char upper and rest of the small
Cap="i Have dont MACbook"
print(Cap.capitalize())
print(Cap.title())
print(Cap.istitle())
rep='i  I have i have a book book'
print(rep.count("have"))
print(rep.count("A"))
print(rep.count("i"))
print(rep.replace('i','me',2))
print(rep.split())
print(rep.startswith('I'))
print(rep.startswith('book'))
print(rep.find('book'))
print(rep.find('fook'))#-1 return if not have

print(rep.index('book'))
#print(rep.index('fook'))# give error if not have
abc='WelcomeToPython3'
print(abc.isalnum())
abc='Welcome To Python3  #!$'
print(abc.isalnum())
abc='WelcomeToPython$567    '
print(abc.isalpha())
print(rep.islower())
print(abc.isprintable())
oo='hii its me puja '
print(oo.isspace())
oo="   "
print(oo.isspace())




