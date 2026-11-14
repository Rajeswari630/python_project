
# Student Record Management System

FILE = "students.txt"


# 1. Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a") as f:
        f.write(sid + "," + name + "," + age + "," + course + "," + marks + "\n")

    print("Student added successfully!")


# 2. View Students
def view_students():
    try:
        with open(FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    if len(lines) == 0:
        print("No student records found.")
        return

    for line in lines:
        data = line.strip().split(",")

        print("\nStudent Details")
        print("ID     :", data[0])
        print("Name   :", data[1])
        print("Age    :", data[2])
        print("Course :", data[3])
        print("Marks  :", data[4])


# 3. Search Student
def search_student():
    sid = input("Enter Student ID: ")
    found = False

    try:
        with open(FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")

                if data[0] == sid:
                    print("\nStudent Found!")
                    print("ID     :", data[0])
                    print("Name   :", data[1])
                    print("Age    :", data[2])
                    print("Course :", data[3])
                    print("Marks  :", data[4])
                    found = True
                    break
    except FileNotFoundError:
        pass

    if not found:
        print("Student not found.")


# 4. Update Student
def update_student():
    sid = input("Enter Student ID to update: ")
    found = False
    new_lines = []

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    for line in lines:
        data = line.strip().split(",")

        if data[0] == sid:
            print("Enter New Details:")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            marks = input("Enter Marks: ")

            new_lines.append(
                sid + "," + name + "," + age + "," + course + "," + marks + "\n"
            )
            found = True
        else:
            new_lines.append(line)

    with open(FILE, "w") as f:
        f.writelines(new_lines)

    if found:
        print("Student updated successfully!")
    else:
        print("Student not found.")


# 5. Delete Student
def delete_student():
    sid = input("Enter Student ID to delete: ")
    found = False
    new_lines = []

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    for line in lines:
        data = line.strip().split(",")

        if data[0] == sid:
            found = True
        else:
            new_lines.append(line)

    with open(FILE, "w") as f:
        f.writelines(new_lines)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main Menu
while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
