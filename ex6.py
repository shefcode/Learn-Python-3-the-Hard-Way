# Exercise 6 - Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# Site 1
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# Site 2
print(f"I said: {x}")
# Site 3
print(f"I also said '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Site 
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
