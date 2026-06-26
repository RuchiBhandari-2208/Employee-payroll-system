class employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary

    def calculate_salary(self):
        hra=0.20*self.basic_salary
        da=0.10*self.basic_salary
        gross_salary=self.basic_salary+hra+da
        return gross_salary

    def display(self):
        print("\nEmployee Details")
        print("Employee ID:",self.emp_id)
        print("Name  :",self.name)
        print("Basic Salary:",self.basic_salary)
        print("Gross Salary:",self.calcuate_salary())
        print("-"*30)

    