students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    total = 0
    num = 0
    for grade in grades:
        total += grade
        num += 1
    av = round(total / num, 2)
    return av

def get_status(avg):
    if avg >= 5.0:
        result = "PASS"
    else:
        result = "FAIL"
    return result

pass_count = 0
fail_count = 0
for student in students:
    aver = round(average(student["grades"]), 1)
    status = get_status(aver)
    name = student["name"]
    print(name, ":",  aver, "->", status)
    if status == "PASS":
        pass_count += 1
    else:
        fail_count += 1
print("Results:", pass_count, "passed,", fail_count, "failed")