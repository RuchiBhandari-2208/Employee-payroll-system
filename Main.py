from Employeepayrollsystem import  Employeepayrollsystem

eps=Employeepayrollsystem()

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
        eps.add_employee()

    elif choice=="2":
        eps.display_employee()

    elif choice=="3":
        eps.search_employee()

    elif choice=="4":
        eps.update_employee()

    elif choice=="5":
        eps.delete_employee()

    elif choice=="6":
        print("Thank You.")
        break

    else:
        print("ivalid choice!please try again.")
        
