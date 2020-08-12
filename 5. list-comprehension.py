temps = [221, 234, 340, 230]

# list comprehension
new_temps = [temp / 10 for temp in temps]

print(new_temps)

# list comprehension with if Conditional
temps2 = [221, 234, 340,-9999, 230]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

## with else
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps ]


print(new_temps)
