def add_student(students):
    name = input("Enter student name: ")

    if name == "":
        print("Student name cannot be empty.")
        return

    students.append({"name": name, "marks": {}})
    print(f"Added student: {name}")


def show_students(students):
    if not students:
        print("No students found.")
        return

    print("\nStudent List")

    for s in students:
        print(f"Name: {s['name']}")


def add_marks(students):
    name = input("Enter student name to add marks: ")

    for s in students:
        if s["name"] == name:
            subject = input("Enter subject: ")

            if subject == "":
                print("Subject cannot be empty.")
                return

            try:
                mark = float(input("Enter mark: "))
            except ValueError:
                print("Please enter a valid number.")
                return

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                return

            s["marks"][subject] = mark
            print("Mark added successfully.")
            return

    print("Student not found.")


def get_average(student):
    if not student["marks"]:
        return 0

    total = 0

    for mark in student["marks"].values():
        total = total + mark

    return total / len(student["marks"])


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def show_report(students):
    if not students:
        print("No report to show.")
        return

    name = input("Enter student name for report: ")

    for s in students:
        if s["name"] == name:
            print(f"\nStudent: {s['name']}")

            if not s["marks"]:
                print("No marks added.")
                return

            for subject, mark in s["marks"].items():
                print(f"  {subject}: {mark}")

            average = get_average(s)
            grade = get_grade(average)

            print("Average:", round(average, 2))
            print("Grade:", grade)
            return

    print("Student not found.")


students = []

while True:
    print("\nStudent Marks Management System")
    print("1: Add student")
    print("2: Show students")
    print("3: Add marks")
    print("4: Show report")
    print("5: Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        show_students(students)

    elif choice == "3":
        add_marks(students)

    elif choice == "4":
        show_report(students)

    elif choice == "5":
        print("Thanks")
        break

    else:
        print("Invalid choice")
