def cylinder_volume(height,radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10,3))

# function return Nne if it doesnt return any value explicitly

def pint_greeting():
    print("Hello World!")
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
print('Done calling')
print('This function returned: {}'.format(1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))
    
# default arguments    
def cylinder_volume1(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2    
# passing value by postion
print(cylinder_volume1(10,7))
print(cylinder_volume1(height = 10,radius = 7))


# write your function here
def population_density(population,land_area):
    return  population / land_area 



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))