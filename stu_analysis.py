# student Analysis code....

marks = []
student = {}

for i in range(10):
    print("\nStudent", i + 1)

    name = input("Enter Name: ")

    while True:
        mark = int(input("Enter Marks (0-100): "))
        if mark >= 0 and mark <= 100:
            break
        else:
            print("Invalid Marks! Enter marks between 0 and 100.")

    marks.append(mark)
    student[name] = mark


marks_tuple = tuple(marks)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)


unique_marks = set(marks)

print("\n========== RESULT ==========")

print("Marks List      :", marks)
print("Marks Tuple     :", marks_tuple)
print("Dictionary      :", student)

print("Highest Marks   :", highest)
print("Lowest Marks    :", lowest)
print("Average Marks   :", round(average, 2))

print("\nStudents Above Average:")
for name, mark in student.items():
    if mark > average:
        print(name, ":", mark)

print("\nUnique Marks :", unique_marks)
