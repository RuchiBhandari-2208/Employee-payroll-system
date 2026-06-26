from EmployeePayrollSystem import Employeeclesystem
emp=Employeepayrollsystem()
while True:
    print("\n======EMPLOYEE PAYROLL SYSTEM======")
    print("1.Add Employee")
    print("2.Display Employee")
    print("3.Search Employee")
    print("4.Update Employee")
    print("5.Delete Employee")
    print("6.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
       emp.add_employee()

    elif choice=="2":
        emp.display_employee()

    elif choice=="3":
        emp.search_employee()

    elif choice=="4":
       emp.update_employee()

    elif choice=="5":
       emp.delete_employee()

    elif choice=="6":
        print("Thank You.")
        break

    else:
        print("ivalid choice!please try again.")
        
