# # first we learn
# file=open("country.txt","w")
# file.write("Italy\n")
# file.write("India\n")
# file.write("BD\n")
# file.write("USA\n")
# file.close()
# file = open("country.txt","r")
# print(file.read())
# file.close()
# file = open("country.txt",'a')
# file.write("France\n")
# file.close()
# # if dont want to use close each time we can use with
# f=open("myfile.txt","a")
# with open("myfile.txt","a") as f:
#     f.write(" hey i am from file mytxt")
#
# #to read each line from a txt file
# f=open("myfile.txt","r")
# while True:
#  line = f.readline()
#  print(line)
#  if not line :
#      break
# ##want to write multiple line at once
# file=open("country.txt","w")
# countries=["bd\n","china\n","india\n","Usa\n"]
# file.writelines(countries)
# ### use loop for entry multiple line
# names = ["Puja", "Ritu", "Anik"]
#
# with open("file1.txt", "w") as f:
#     for name in names:
#         f.write(name + "\n")
# seek funtion + tell()
with open("myfile.txt", "r") as file:
    current_position=file.tell()
    print(current_position)
    file.seek(current_position)  # from which we want to read
    data = file.read(5)
    print(data)
    file.seek(10)
    data = file.read(5)
    now=file.tell()
    print(now)
    print(data)

    # tr
