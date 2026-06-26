from Employee import employee

class Employeesystem:
    def __init__(self):
        self.employees=[]
    
    def add_employee(self):
        emp_id = int(input("Enter Employee id:"))
        name =(input("Enter your name:"))
        basic_salary=(input("Enter your basic salary:"))

        employee = employee(self,emp_id,name,basic_salary)
        self.employees.append(employee)

    def display_employee(self):
        print("display employee:")

    def search_employee(self):
        print("search employee:")

    def update_salary(self):
        print("update salary:")

    def delete_employee(self):
        print("delete employee:")


