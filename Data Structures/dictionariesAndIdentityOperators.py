# Simple Dictionary where keys are element name and  their corresponding values are atomic number

elements = {'hydrogen':1, 'helium':2, 'carbon':6}
print(elements['carbon'])
# inserting new value in dictionary
elements['lithium'] = 3
print(elements)

# checking element in dictionary using in keyword
print('mithril' in elements)

# using get() method 
x = elements.get('dilithium')
print(x)

#return output of choice if element not found via get() method
print(elements.get('kryptonite', 'There\'s no such element!'))

# using Identity operator to know if get element return none or not
is_null = x is None
print(is_null)

# checking opposite
not_null = x is not None
print(not_null) 


# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai':17.8 ,'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}

# diffrence in "is" and ==
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)