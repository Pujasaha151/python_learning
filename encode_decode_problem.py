import random
from ctypes.wintypes import tagMSG
encode=input("enter a sms u want to send->")
x=len(encode)
print(x)
if x>=3:
  temp=(list(encode))
  print(temp)
  x=temp.pop(0)
  print(temp)
  temp.append(x)
  print(temp)
  st="vdcuehxodb"
  st1='YDEGXEUHC'
  ran=random.sample(st,3)
  ran1 = random.sample(st1, 3)
  new=ran+temp+ran1
  print(new)
  new.reverse() 
  print(new)
sms="".join(new)
print(sms)
# decoder part
new.reverse()
print(new)
then=new[3:-3]
print(then)
x = then.pop()
print(then)
then.insert(0,x)
print(then)
decode="".join(then)
print("the received sms is :",decode)










