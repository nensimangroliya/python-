# Student Performance Analytics System

students = []
grade_dict = {}

subjects = ["Big Data", "OS", "Java", "C++", "Python"]
subject_total = [0, 0, 0, 0, 0]

# Input 10 Students
for i in range(10):

    print("\nStudent", i + 1)

    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    marks = []

    # Input Marks with Validation
    for j in range(5):

        while True:
            mark = int(input("Enter " + subjects[j] + " Marks (0-100): "))

            if mark >= 0 and mark <= 100:
                marks.append(mark)
                subject_total[j] += mark
                break
            else:
                print("Invalid Marks! Please enter marks between 0 and 100.")

    
    total = sum(marks)
    percentage = total / 5

   
    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

   
    students.append({
        "roll": roll,
        "name": name,
        "marks": tuple(marks),
        "total": total,
        "per": percentage,
        "grade": grade
    })


class_avg = 0
for s in students:
    class_avg += s["per"]

class_avg = class_avg / len(students)

print("\n========== RESULT ==========")

print("\nClass Average:", round(class_avg, 2))


high = max(s["total"] for s in students)

print("\nHighest Scorer:")
for s in students:
    if s["total"] == high:
        print(s["name"], "-", s["total"])


low = min(s["total"] for s in students)

print("\nLowest Scorer:")
for s in students:
    if s["total"] == low:
        print(s["name"], "-", s["total"])


print("\nStudents Above Average:")
for s in students:
    if s["per"] > class_avg:
        print(s["name"])


print("\nFailed Students:")
for s in students:
    if min(s["marks"]) < 40:
        print(s["name"])


for s in students:
    if s["grade"] not in grade_dict:
        grade_dict[s["grade"]] = []

    grade_dict[s["grade"]].append(s["name"])

print("\nGrade Wise Students:")
print(grade_dict)


names = []

for s in students:
    names.append(s["name"])

names.sort()

print("\nNames in Alphabetical Order:")
for name in names:
    print(name)


first = 0
second = 0

for s in students:
    if s["total"] > first:
        second = first
        first = s["total"]
    elif s["total"] > second and s["total"] != first:
        second = s["total"]

print("\nSecond Highest Scorer:")
for s in students:
    if s["total"] == second:
        print(s["name"], "-", s["total"])

avg = []

for total in subject_total:
    avg.append(total / len(students))

highest_avg = max(avg)
index = avg.index(highest_avg)

print("\nSubject with Highest Average:")
print(subjects[index], "-", round(highest_avg, 2))


name_list = []
duplicate = set()

for s in students:
    name_list.append(s["name"])

for name in name_list:
    if name_list.count(name) > 1:
        duplicate.add(name)

print("\nDuplicate Names:")
if len(duplicate) == 0:
    print("No Duplicate Names")
else:
    print(duplicate)