mv_population = 74728
x = 2
y = 2
print(y)
x = 2
y = 3
z = 5
x,y,z = 2,3,5 

# To calculate Population density in mountain view
x = 74728
y = 11.995
z= x/y
print(z) 

# Program will be much clearer with these variable names

mv_population = 74728
mv_area = 11.995
mv_density = mv_population / mv_area
print(mv_density)

# mv_population = mv_population + 4000 - 600
mv_population +=  4000 - 600

# Note that this code uses scientific notation 
# to define large numbers. 4.445e8 is equal to 
# 4.445 * 10 ** 8 which is equal to 444500000.0.
print(50-50/10)
print(4.445e8)


# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= rainfall/10

# add the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += reservoir_volume/5
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume/5
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)