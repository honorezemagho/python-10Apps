import datetime
mynow = datetime.datetime.now()
print(mynow)

#Integer
x = 10

#String
y = '10'

#Float
z = 10.1
 
# List datastructure
monday_temperature = [9.1,8.8,9.9]

#Dictionary Datastructure
student_grades = {"Mary": 9.1, "Six": 8.8, "John": 7.5}

#Tuple datastructure (it a kind with paranthesis, tuples are immutable
# but list are mutable)
monday_temperature_tuple = (9.1,8.8,7.5)



sum1 = x + x
sum2= y + y 
length = len(monday_temperature)
mysum = sum(monday_temperature)
mean = mysum / length

print(mean)

print(sum1, sum2)
# type() is used to define the type of a variable
print(type(x), type(y), type(z))

#Access to the portion of the list (Slice)
#monday_temperature[0:2]  the first two items of the list
#monday_temperature[:2] shorthand for the first two items
#monday_temperature[3:] shorthand for taking the items from 3 to the end of the list

#We can check elements index by negation
# e.g: monday_temperature[-1] for the last element of the list

#You can also find the element index of a string
#e.g: mystring = 'hello'
# mystring[1] return 'e'

#You have the possibility to chain indexes of a list
#e.g monday_temperatures = ['hello',1,2,3]
#monday_temperatures[0][2] return 'l'

#Accessing Items in Dictionaries
print(student_grades["Six"]) #8.8

#Creating your own functions
# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# mean_result = mean([1,4,7])
# print(mean_result)

#When your function doesn't have a return it's implicitely return a "None" object. which means nothing
# You should always have a return in your function

# If conditional example
def mean(value):
    if isinstance(value, dict): # or type(value) == dict: 
        the_mean = sum(value.values()) / len(value)
    elif isinstance(value, list):
        the_mean = sum(value) / len(value)
    else:
        the_mean = value
    return the_mean

print(mean(student_grades)) 
print(mean(monday_temperature)) 

# after a colum you always have inentation