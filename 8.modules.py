import  time
import os
import pandas

# while True:
#     if os.path.exists("files/vegetables.txt"):

#         with open("files/vegetables.txt") as file:
#             print(file.read())
     
#     else:
#         print("File not found")
#         time.sleep(10)


while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
     
    else:
        print("File not found")
        time.sleep(10)