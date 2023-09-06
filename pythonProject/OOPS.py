class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = []
for i in range(3):
    name = input("Enter your name: ")
    try:
        salary = int(input("Enter Your salary: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric salary.")
        salary = 0


employee_obj = Employee(name, salary)
employees.append(employee_obj)

for employee_obj in employees:
    print("Your name is:", employee_obj.name)
    print("Your Salary is:", employee_obj.salary)
