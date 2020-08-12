monday_temperatures = [9.1,8.0,7.6]

# A for loop iterate inside a container. it could a list, string, tuple or dictionnary
# For in loop

## Looping inside a list
for temperature in monday_temperatures:
    print(round(temperature))
print("Done")

for letter in 'hello':
    print(letter)

## Looping inside a dictionary
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

### Looping dictionary items
for grades in student_grades.items():
    print(grades)

### Looping dictionary keys
for grades in student_grades.keys():
    print(grades)

### Looping dictionary values
for grades in student_grades.values():
    print(grades)



# A for loop runs until a container is exausted and
#  a while loop runs as long as this condition is true

# While  loop
# username = ''

# while username != "pypy":
#     username = input("Enter username: ")

## While loop with Break and Continue
while True:
    username = input("Enter Username: ")
    if username == 'pypy':
        print("Sucess %s. You've done Great Job" % username)
        break
    else:
        print("Wrong username %s. Please try again" % username)
        continue
