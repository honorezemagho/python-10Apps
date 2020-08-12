
# Read File once
myfile = open("files/fruits.txt")
# print(myfile.read())

## Read file many times 
content = myfile.read()

# print(content)
# print(content)

# when you create a file object, it's going to be created in RAM and
#  remain until the execution of your program end

# Closing a file
myfile.close()

#Opening file using with 
# with open('files/fruits.txt') as myfile:
#     content = myfile.read()

# print(content)

# writing a text file
with open('files/vegetables.txt','w') as vegetables:
        # vegetables.write("Tomatoes") # Single element
    vegetables.write("Tomatoes\nCarrots\nCumcumber\nAbricot\nGarlic") # multiple elements


#Appending text to an existing file
with open('files/fruits.txt','a+') as fruits:
        # fruits.write("\nBanana") # Single
    fruits.write("\nPineapple\nCarrots\nCumcumber\nAbricot") # multiple
    fruits.seek(0)
    content = fruits.read()

    print(content)





