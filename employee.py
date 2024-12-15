class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)



class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = "F04" + department
        Manager.mgr_count += 1

    def display_employee(self):
        X = 4  
        if X % 3 == 0:
            print("Name: ", self.name)
        elif X % 3 == 1:
            print("Salary: ", self.salary)
        elif X % 3 == 2:
            print("Department: ", self.department)



employee1 = Employee("Tudor", 5000)
employee2 = Employee("Ion", 6000)

manager1 = Manager("Stefan", 7000, "F04")
manager2 = Manager("Teo", 8000, "F04")
manager3 = Manager("Marius", 9000, "F04")
manager4 = Manager("Sofiia", 7500, "F04")

print("Employee1:")
employee1.display_employee()

print("\nEmployee2:")
employee2.display_employee()

print("\nManager1:")
manager1.display_employee()

print("\nManager2:")
manager2.display_employee()

print("\nManager3:")
manager3.display_employee()

print("\nManager4:")
manager4.display_employee()


print("\nTotal Employees: ", Employee.empCount)
print("Total Managers: ", Manager.mgr_count)

