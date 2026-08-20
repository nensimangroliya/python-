# Student Information System..........
def marks(subject):
    while True:
        try:
            mark = float(input("Enter " + subject + " Marks: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid Marks! Enter 0 to 100.")

        except ValueError:
            print("Please enter numeric marks only.")

students = []

n = int(input("Enter Number of Students: "))

for i in range(n):

    print("\nStudent", i + 1)

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    print("\nEnter Subject Marks")

    big_data = marks("Big Data")
    os = marks("Operating System")
    java = marks("Java")
    php = marks("php")
    python = marks("Python")

    total = big_data + os + java + php + python
    percentage = total / 5

    if (big_data >= 40 and os >= 40 and java >= 40 and
        php >= 40 and python >= 40):
        result = "PASS"
    else:
        result = "FAIL"

    if result == "FAIL":
        grade = "F"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"

    students.append([roll, name, age, total, percentage, result, grade])

print("\n========== Student Result ==========")

for student in students:
    print("--------------------------------")
    print("Roll Number :", student[0])
    print("Name        :", student[1])
    print("Age         :", student[2])
    print("Total Marks :", student[3], "/500")
    print("Percentage  : {:.2f}%".format(student[4]))
    print("Result      :", student[5])
    print("Grade       :", student[6])

print("--------------------------------")
