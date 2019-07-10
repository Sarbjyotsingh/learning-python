card_deck = [4,11,8,5,13,2,8,10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number >= current:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1



# print the factorial of number
print(product)

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for num in range(1,7):
    product *= num


# print the factorial of number
print(product)


start_num = 5 #provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 10#provide some number to count by  
break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
while break_num < end_num:
    break_num += count_by 



print(break_num)


start_num =5 #provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 10#provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
result = start_num
if end_num < start_num:
    print("Oops! Looks like your start value is greater than the end value. Please try again.")
else:
    while result < end_num:
        result += count_by 


print(result)

limit = 40

num = 0
# write your while loop here
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

## Please use this space to test and run your code

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd = 0
i = 0
while odd == 5 or i<len(num_list) :
    if(num_list[i] %2 != 0):
        odd+=num_list[i]
    i += 1
print(odd)
    