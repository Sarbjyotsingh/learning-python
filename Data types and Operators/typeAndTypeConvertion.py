# Same number can be coded in diffrent type
# each of their own set of behaviour

print(type(633))
print(type(633.))
print(type("633"))


# We can create new objects from old and change it's type

count  = int(4.0) 
print(count)
print(type(count)) 

# createing larger string
house_number = 13
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))

address = str(house_number) + " " + street_name + ", " + town_name
print(address)

# Converting str to float
grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))
print(grams)



mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: "+ str(total_sales))