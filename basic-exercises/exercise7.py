student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])

print("Number of subjects:", len(student["subjects"]))

flag = False
if "PNE" in student["subjects"]:
    flag = True
print("Enrolled in PNE:", flag)

print("Databases grade:", student["grades"]["Databases"])

total = 0
num = 0
for subject, grade in student["grades"].items():
    total += grade
    num += 1
average = round((total / num), 2)
print("Average grade:", average)

print("Subject grades:")
for subject, grade in student["grades"].items():
    print(subject, ":", grade)