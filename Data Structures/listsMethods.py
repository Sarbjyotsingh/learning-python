# in Strings
name = 'Jim'
student = name
name = 'Tim'

print(name)
print(student)

# mutataion reflects in lists
scores =["B", "C", "A", "D", "B", "A"]
grades = scores
print("scores: " + str(scores))
print("grades: " + str(grades))
scores[3] = "B"
print("scores: " + str(scores))
print("grades: " + str(grades))

# max() function
# for list of number max is largest number

batch_size = [15,6,89,34,65,35,23.4]
print(max(batch_size))
print(len(batch_size))

# for strings greatest element would be element that would occur last if list is sorted alphabatically
python_varities = ["Hello", "These", "Working","Random", "Guys"]

print(max(python_varities))

# min() function return minimum object of list
print(min(batch_size))

# sorted() return copy of list in ordered form leaving orignal list unchanged

# assending order
print(sorted(batch_size))

# decending order
print(sorted(batch_size,reverse = True))

# join() function return string with list element joined by seprator string
nutical_direction  = "\n".join(["fore", "aft", "starboard", "port"])
print(nutical_direction)

# append() function

batch_size.append(55)
print(batch_size)