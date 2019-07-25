def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius

# using function three times
cylinder_volume(10, 3)
cylinder_volume(11, 4)
cylinder_volume(12, 5)

# writing the cylinder volume formula three times
pi = 3.14159 
10 * pi * 3 ** 2
11 * pi * 4 ** 2
12 * pi * 5 ** 2

# documentation string or doc string 
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
def population_density1(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area    


# The first line of the docstring is a brief explanation of the function's purpose. 
# If you feel that this is sufficient documentation you can end the docstring at this point   
# If you think that a longer description would be appropriate for the function, you can add more information 
# after the one-line summary. In the example above, you can see that we wrote an explanation of the function's 
# arguments, stating the purpose and types of each one. It's also common to provide some description of the 
# function's output. 


def readable_timedelta(days):
    """
    Calculate the Number of weeks and days in given number of days   
    Input:
    days : int The number of days whose week is to be calculated     
    Output:
    Print the string whuch tell number of days and week in given number of days    
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)