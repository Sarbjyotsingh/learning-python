# Simple List declaration
months = ['January', 'February','March','April','May','June','July', 
          'August','September', 'October', 'November', 'December']
# indexing
print(months[0])
print(months[1])
print(months[7])

# indexing from end of list
print(months[-1])
print(months[-0]) # work as 0th index

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])

# retriveing last element by reducing index by 1 
print(list_of_random_things[len(list_of_random_things) - 1])

# Alternative
print(list_of_random_things[-1])

# Slicing lists
q3 = months[6:9]
print(q3)
# lower bound is inclusive and upper bound is exclusive

# coomon shortcuts of slicing
first_half = months[:6]
print(first_half) 

second_half = months[6:]
print(second_half)

# comparing functions of lists and strings
greet = "Hello there"

print(len(greet), len(months))
print(greet[6:9], months[6:9])

# Membership operators "in" "not in"
print('her' in greet, 'her' not in greet)
print('Sunday' in months, 5 not in months)
print(5 not in [1, 2, 3, 4, 6])

# lists are mutable while strings are unmutable
months[3] = 'Friday'
print(months)

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)


# Use list indexing to determine how many days are in a particular month based on the integer variable month, 
# and store that value in the integer variable num_days. For example, if month is 8, num_days should be set 
# to 31, since the eighth month, August, has 31 days.

# Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month-1]
print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])