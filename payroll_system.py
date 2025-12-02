
employees = []   # arraylist


def find_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None


def input_positivenumber(Answer):
    while True:
        value = input(Answer)
        try:
            value = float(value)
            if value >= 0:
                return value
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Invalid number. Try again.")

def main_menu():
    while True:
        print("========== MAIN MENU ==========")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. View Employee")
        print("5. Payroll Calculation")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            edit_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            view_employee()
        elif choice == "5":
            payroll_calculation()
        elif choice == "6":
            print("Program Terminated.")
            break
        else:
            print("Invalid input. Try again.")

def add_employee():
    print("--- ADD EMPLOYEE ---")
    emp_id = input("Input Employee ID: ").strip()
    name = input("Input Name: ").strip()
    position = input("Input Position: ").strip()

    rate = input_positivenumber("Input Rate per Hour: ")

    print("\nPlease confirm the following:")
    print(f"ID: {emp_id}")
    print(f"Name: {name}")
    print(f"Position: {position}")
    print(f"Rate: {rate}")
    confirm = input("Save? (Y/N): ").lower()

    if confirm == "y":
        employees.append({
            "id": emp_id,
            "name": name,
            "position": position,
            "rate": rate
        })
        print("Employee saved!")
    else:
        print("Cancelled.")

def edit_employee():
    print("--- EDIT EMPLOYEE ---")
    emp_id = input("Search by ID: ").strip()
    emp = find_employee(emp_id)

    if not emp:
        print("No data found.")
        return

    print("Updating Employee Data...")
    emp["name"] = input("Update Name: ").strip()
    emp["position"] = input("Update Position: ").strip()
    emp["rate"] = input_positivenumber("Update Rate per Hour: ")

    print("Updated Record:")
    print(emp)
    confirm = input("Save changes? (Y/N): ").lower()
    if confirm == "y":
        print("Record updated.")
    else:
        print("Update cancelled.")

def delete_employee():
    print("--- DELETE EMPLOYEE ---")
    emp_id = input("Search by ID: ").strip()
    emp = find_employee(emp_id)

    if not emp:
        print("No data found.")
        return

    print(f"Are you sure you want to delete {emp['name']}?")
    confirm = input("Confirm delete? (Y/N): ").lower()

    if confirm == "y":
        employees.remove(emp)
        print("Record deleted.")
    else:
        print("Deletion cancelled.")

def view_employee():
    print("--- VIEW EMPLOYEE ---")
    print("1. View All Employees")
    print("2. Search Specific Employee")
    ch = input("Choose option: ")

    if ch == "1":
        if not employees:
            print("No employees found.")
        else:
            print("--- ALL EMPLOYEES ---")
            for emp in employees:
                print(emp)
            print()

    elif ch == "2":
        emp_id = input("Input ID for searching: ")
        emp = find_employee(emp_id)
        if not emp:
            print("Employee not found.")
        else:
            print("--- EMPLOYEE FOUND ---")
            print(emp)
            print()

    else:
        print("Invalid option.")

def payroll_calculation():
    print("--- PAYROLL CALCULATION ---")

    if not employees:
        print("No employees available.")
        return

    print("Available Employees:")
    for emp in employees:
        print(f"ID: {emp['id']}  Name: {emp['name']}")

    emp_id = input("Select an Employee ID: ")
    emp = find_employee(emp_id)
    if not emp:
        print("Employee not found.")
        return

    hours = input_positivenumber("Input Hours Worked: ")

    gross = hours * emp["rate"]
    deduction = gross * 0.10  
    net = gross - deduction

    print("--- PAYROLL RECORD ---")
    print(f"Employee: {emp['name']}")
    print(f"Hours Worked: {hours}")
    print(f"Rate: {emp['rate']}")
    print(f"Gross Pay: {gross}")
    print(f"Deduction: {deduction}")
    print(f"Net Pay: {net}")



main_menu()
