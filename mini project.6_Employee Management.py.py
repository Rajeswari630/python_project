# Employee Management System using OOPs concepts
def main():
    print("===== Employee Management System =====")
    print("1. Developer")
    print("2. Manager")
    print("3. Tester")

    choice = int(input("Enter your choice: "))

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    if choice == 1:
        language = input("Enter Programming Language: ")
        project = input("Enter Project Name: ")
        experience = int(input("Enter Experience: "))
        emp = Developer(emp_id, name, basic_salary, language, project, experience)

    elif choice == 2:
        department = input("Enter Department: ")
        team_size = int(input("Enter Team Size: "))
        experience = int(input("Enter Experience: "))
        emp = Manager(emp_id, name, basic_salary, department, team_size, experience)

    elif choice == 3:
        tool = input("Enter Testing Tool: ")
        experience = int(input("Enter Experience: "))
        test_type = input("Enter Testing Type: ")
        emp = Tester(emp_id, name, basic_salary, tool, experience, test_type)

    else:
        print("Invalid choice!")
        return

    final_salary = emp.calculate_salary()
    bonus = final_salary - emp.basic_salary

    print("\n===== Employee Details =====")
    emp.display_details()
    print("Bonus              : ₹", int(bonus), sep="")
    print("Final Salary       : ₹", int(final_salary), sep="")


class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_details(self):
        print("Employee ID        :", self.emp_id)
        print("Employee Name      :", self.name)
        print("Basic Salary       : ₹", self.basic_salary, sep="")

    def calculate_salary(self):
        return self.basic_salary


class Developer(Employee):
    def __init__(self, emp_id, name, basic_salary, language, project, experience):
        super().__init__(emp_id, name, basic_salary)
        self.language = language
        self.project = project
        self.experience = experience

    def display_details(self):
        super().display_details()
        print("Role               : Developer")
        print("Programming Lang.  :", self.language)
        print("Project Name       :", self.project)
        print("Experience         :", self.experience, "Years")

    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Manager(Employee):
    def __init__(self, emp_id, name, basic_salary, department, team_size, experience):
        super().__init__(emp_id, name, basic_salary)
        self.department = department
        self.team_size = team_size
        self.experience = experience

    def display_details(self):
        super().display_details()
        print("Role               : Manager")
        print("Department         :", self.department)
        print("Team Size          :", self.team_size)
        print("Experience         :", self.experience, "Years")

    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Tester(Employee):
    def __init__(self, emp_id, name, basic_salary, tool, experience, test_type):
        super().__init__(emp_id, name, basic_salary)
        self.tool = tool
        self.experience = experience
        self.test_type = test_type

    def display_details(self):
        super().display_details()
        print("Role               : Tester")
        print("Testing Tool       :", self.tool)
        print("Testing Type       :", self.test_type)
        print("Experience         :", self.experience, "Years")

    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.15


main()
