# Using if keyword

phone_balance = 3
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -=10

print(phone_balance,bank_balance)

# Using Else Keyword
n = 5
if n%2 == 0:
    print("Number " + str(n) + " is even.")
else:
    print("Number " + str(n) + " is odd.")

season = "winter"

if season == "spring":
    print("Plant the garden!")
elif season == "summer":
    print("water the garden!")
elif season == "fall":
    print("harvest the garden!")
elif season == "winter":
    print("stay indoors!")
else:
    print("Unrecognized season")
           

           #First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

# 
points = 174  # use this input to make your submission

# write your if statement here
if points <= 1  and points >=50:
    result = "wooden rabbit"
elif points <= 51  and points >=150:
    result = None
elif points <= 151  and points >=180:
    result = "wafer-thin mint"
elif points <= 151  and points >=180:
    result = "wafer-thin mint"    
else:
    result = "penguin"

if result != None:
    print("Congratulations! You won a {}!".format(result))
else:
    print("Oh dear, no prize this time.")

print(result)

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''

answer = 30
guess = 35

if guess<answer:
    result = "Oops!  Your guess was too low."
elif guess>answer:
    result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"

print(result)


points = 174  # use this as input for your submission


# establish the default prize value to None
price = None

# use the points value to assign prizes to the correct prize names

if points <= 50:
    price = "wooden rabbit"
elif points <= 150:
    price = None
elif points <= 180:
    price = "wafer-thin mint"
else:
    result = "penguin"
# use the truth value of prize to assign result to the correct prize

if price:
    result = "Congratulations! You won a {}!".format(price)

print(result)