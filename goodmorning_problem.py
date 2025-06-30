import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=int(time.strftime("%H"))

if(4<timestamp<12):
  print("good morning")
elif(12<(timestamp)<19):
    print("good afternoon")
else:
    print('good night')

