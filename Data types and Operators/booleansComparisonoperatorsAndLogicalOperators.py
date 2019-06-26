# Assigment of boolean value
the_sun_is_up = True
this_sun_is_blue = False

# Creating Boolean result with Comparsion Operators
x = 42 > 43
print(x)

# using Logical operators with Comparison operators to evaluate boolean result
age = 14
is_teen = age > 12 and age<20
print(is_teen)

# inversiing result using NOT
is_teen = not(age > 12 and age<20)
print(is_teen)


# Write code to compare these densities.
# Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

print(san_francisco_pop_density > rio_de_janeiro_pop_density)