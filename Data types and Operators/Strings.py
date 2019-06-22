# we can create String by using quotes
# single or double quotes work equally
print("hello") # single quotes
print('hello') # double quotes

# String variable
Welcome_message = "Welcome to Learning python"
print(Welcome_message)

# Putting quotation marke in String if we do it directly Syntax Error will Occur

# 1st Solution
Message1 = "Hello How are'YOU'"
Message2 = 'Hello How are"YOU"'
print(Message1)
print(Message2)

# 2nd Solution wusing forwardslash
salesman = 'I Think you\'re Salesman'
print(salesman)

# Using Operation on String: + and *
first_word  = "Hello"
Second_word = "There"
print(first_word+" "+Second_word)

# Inbuilt Function for calculating length of string
length = len("Working")
print(len("ababa") / len("ab"))

# Indexing in Strings
print(Message1[0])

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'


username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site "+"http://petshop.com/pets/mammals/cats"+" at "+timestamp+".")
