# Exercise 5 - More Variables and Printing

name = 'Nymphadora Tonks'
age = 47
height = round(66 * 2.54, 2) # inches to cm 
weight = round(126 * 2.205, 2) # lbs to kg
eyes = 'Brown'
teeth = 'White'
hair = 'Light Brown'

print(f"Let's talk about {name}.")
print(f"She is {height} centimeter tall.")
print(f"She is {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

total = round(age + height + weight, 2)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
