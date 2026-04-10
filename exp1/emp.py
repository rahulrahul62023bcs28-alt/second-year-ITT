def display_menu():
    print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Exit")

def main():
    employees = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add Employee
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = input("Enter Salary: ")

            employee = {
                "id": emp_id,
                "name": name,
                "dept": dept,
                "salary": salary
            }
            employees.append(employee)
            print("Employee added successfully!")

        elif choice == '2':
            # View All Employees
            if not employees:
                print("\nNo employee records found.")
            else:
                print("\n--- Employee List ---")
                for emp in employees:
                    print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['dept']} | Salary: {emp['salary']}")

        elif choice == '3':
            # Search by ID
            search_id = input("Enter Employee ID to search: ")
            found = False
            for emp in employees:
                if emp['id'] == search_id:
                    print(f"\nRecord Found: ID: {emp['id']}, Name: {emp['name']}, Dept: {emp['dept']}, Salary: {emp['salary']}")
                    found = True
                    break
            if not found:
                print("Employee ID not found.")

        elif choice == '4':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
