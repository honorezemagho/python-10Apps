# Function with multiples arguments
def area(a,b):
    return a * b

# Default Parameter
    # A default Parameter cannot be before non-default parameter
def area(a,b=6):
    return a * b

## non - keywords arguments / Positional Arguments (They don't have leywords attach to them)
print(area(4,5))
print(area(5))

## keywords arguments
print(area(a=12,b=5))


# Function with arbitrary number of non-keywords argument
def mean(*args):
    return sum(args) / len(args)

print(mean(1,45,5.8,75,14))

# Function with arbitrary number of keywords argument
def mean(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

print(mean(z=1,x=45,y=5.8,f=75,a=14))