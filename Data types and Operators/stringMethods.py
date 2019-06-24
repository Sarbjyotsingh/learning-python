name = "Sarbjyot singh chahal"

# title()  method
print(name.title())

# islower() method
print(name.islower())

# count() method it takes more argument than just the object
print("One fish, two fish, red fish, blue fish.".count('fish'))

# find() method
print(name.find('s'))

# No professional has all the methods memorized, which is why understanding how to use documentation and find answers
# is so important. Gaining a strong grasp of the foundations of programming will allow you to use those foundations to 
# use documentation to build so much more than someone who tries to memorize all the built-in methods in Python.

# format() method

print("Mohammed has {} balloons".format(27))

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))


# format Exmaples

print("{}, {}, {}".format('a', 'b', 'c'))

print("{0}, {1}, {2}".format('a', 'b', 'c'))

print("{2}, {0}, {1}".format('a', 'b', 'c'))

print("{2}, {0}, {1}".format(*'abc'))

print('{0}{1}{0}'.format('abra', 'cad'))

# argument name in format

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here
string = "sarbjyot singh chahal"

print(string.capitalize())

print(string.casefold())

print(string.isdecimal())

print(string.isdigit())

print(string.isidentifier())

print(string.islower())



# Write two lines of code below, each assigning a value to a variable


#  Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables

print("Sarbjyot {} {}".format("Singh", "chahal"))

print("Sarbjyot {1} {0}".format("chahal","Singh"))

print("Sarbjyot {6} {0}".format(*"chahalSingh"))

caste = {'Second':'Singh','third':'Chahal'}
print("Sarbjyot {Second} {third}".format(**caste))


# Split() method

new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))
print(new_str.split('.'))
print(new_str.split(None, 3))


# \n is a special sequence of characters that causes a line break (a new line).


# 1 What is the length of the string variable verse?
# 2 What is the index of the first occurrence of the word 'and' in verse?
# 3 What is the index of the last occurrence of the word 'you' in verse?
# 4 What is the count of occurrences of the word 'you' in the verse?

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))



verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))