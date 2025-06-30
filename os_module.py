import os

if (not os.path.exists("data")):
    os.mkdir("data")
for i in range(0, 5):
    os.mkdir(f"data/Day{i + 1}")

## to rename
for i in range(0, 5):
    os.rename(f"data/Day{i + 1}", f"data/pora{i + 1}")
    # to enter each folder
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(os.listdir(f"data/{folder}"))
    # to get directory
    print(os.getcwd)