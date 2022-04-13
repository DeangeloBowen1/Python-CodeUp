import json

students = list(json.load(open('students.json')))

# printing dictionary of profiles from json

print(students[0].keys())
print(students[0].values())

"""---------------------------------------------------------------------------------------------------------------------
How many students are there?
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

num_students = len(students)
print("{} students".format(num_students))


"""---------------------------------------------------------------------------------------------------------------------
How many students prefer light coffee?
---------------------------------------------------------------------------------------------------------------------"""
print(" ")
coffee = 0
for student in students:
    if student["coffee_preference"] == 'light':
        coffee = coffee + 1
print("{} students prefer light coffee out of all 3 types".format(coffee))


"""---------------------------------------------------------------------------------------------------------------------
How many types of each pet are there?
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

pets = []
for student in students:
    for pet in student['pets']:
        pets.append(pets['species'])

print(pets)









