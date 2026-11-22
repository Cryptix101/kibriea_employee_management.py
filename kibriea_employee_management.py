# Employee Salary Management System
# Author: Kibriea
# Objective: Practice Python Functions, Parameters, Return Statements, and File Handling (r, a modes).

FILE_NAME = "employees.txt"


def format_employee_record(name, emp_id, salary):
    """
    Format employee details into 'Name | ID | Salary' string format
    and return the formatted line.
    """
    clean_name = name.strip()
    clean_id = emp_id.strip()
    clean_salary = salary.strip()
    return f"{clean_name} | {clean_id} | {clean_salary}\n"


def add_employee(name, emp_id, salary, filename=FILE_NAME):
    """
    Append a new employee record to the text file using 'a' (append) mode.
    Returns True if saved successfully, otherwise False.
    """
    record = format_employee_record(name, emp_id, salary)

    try:
        # 'a' mode creates the file if it doesn't exist and appends new records at the end
        with open(filename, "a", encoding="utf-8") as file:
            file.write(record)
        return True
    except OSError as error:
        print(f"File write error: {error}")
        return False


def view_employees(filename=FILE_NAME):
    """
    Read employee records from the text file using 'r' (read) mode.
    Returns a list of non-empty record lines.
    """
    try:
        # 'r' mode opens the file for reading existing records
        with open(filename, "r", encoding="utf-8") as file:
            records = [line.strip() for line in file if line.strip()]
        return records
    except FileNotFoundError:
        # Return an empty list if employees.txt has not been created yet
        return []
    except OSError as error:
        print(f"File read error: {error}")
        return []


def is_valid_salary(salary_input):
    """
    Validate that salary is a positive number (integer or decimal).
    Returns True if valid, otherwise False.
    """
    try:
        value = float(salary_input)
        return value > 0
    except ValueError:
        return False


def display_menu():
    """Display the main menu options."""
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")


def handle_add_employee():
    """Collect user inputs, validate data, and call add_employee()."""
    name = input("Enter Name: ").strip()
    emp_id = input("Enter ID: ").strip()
    salary = input("Enter Salary: ").strip()

    if not name or not emp_id:
        print("Name and ID cannot be empty.")
        return

    if not is_valid_salary(salary):
        print("Invalid salary. Please enter a positive number.")
        return

    saved = add_employee(name, emp_id, salary)
    if saved:
        print("Employee Added Successfully")
    else:
        print("Failed to add employee.")


def handle_view_employees():
    """Fetch records using view_employees() and print them cleanly."""
    records = view_employees()
    if not records:
        print("No employee records found.")
        return

    print("\n--- Employee Records ---")
    for record in records:
        print(record)


def main():
    """Main program loop controlling user choices."""
    while True:
        display_menu()
        choice = input("Choose Option: ").strip()

        if choice == "1":
            handle_add_employee()
        elif choice == "2":
            handle_view_employees()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
