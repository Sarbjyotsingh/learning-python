AngkorWat = (13.4125, 103.866667)

print(type(AngkorWat))

print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

# when making tuples paranthesis are optional
# tuples are used to assign mutiple variable in compact way

diemsions = 52, 40, 100
length, width, height = diemsions  # This is called tuple unpacking
print("The dimensions are {}x{}x{}".format(length,width,height))