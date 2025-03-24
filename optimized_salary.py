class Employee:
    """Base class representing an employee."""
    def __init__(self, emp_id: int, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self) -> float:
        """Returns the salary of the employee."""
        return self.salary

    def __str__(self) -> str:
        """Returns a string representation of the employee."""
        return f"{self.name}'s salary: ${self.calculate_salary():.2f}"


class HourlyEmployee(Employee):
    """Represents an employee paid on an hourly basis."""
    def __init__(self, emp_id: int, name: str, hourly_rate: float, hours_worked: float):
        salary = hourly_rate * hours_worked  # Calculate total salary
        super().__init__(emp_id, name, salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        """Overrides the method to calculate salary based on hourly rate and hours worked."""
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    """Represents an employee with a fixed monthly salary."""
    def __init__(self, emp_id: int, name: str, monthly_salary: float):
        super().__init__(emp_id, name, monthly_salary)


def get_valid_input(prompt: str, data_type: type) -> float:
    """Handles user input validation to ensure correct data type is entered."""
    while True:
        try:
            value = data_type(input(prompt))
            if isinstance(value, (int, float)) and value < 0:
                print("Value cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")


def main():
    """Main function to get user input and display salary calculations."""
    print("Enter details for Hourly Employee:")
    emp_id = get_valid_input("Enter Employee ID: ", int)
    name = input("Enter Employee Name: ").strip()
    hourly_rate = get_valid_input("Enter Hourly Rate: ", float)
    hours_worked = get_valid_input("Enter Hours Worked: ", float)

    hourly_emp = HourlyEmployee(emp_id, name, hourly_rate, hours_worked)

    print("\nEnter details for Salaried Employee:")
    emp_id = get_valid_input("Enter Employee ID: ", int)
    name = input("Enter Employee Name: ").strip()
    monthly_salary = get_valid_input("Enter Monthly Salary: ", float)

    salaried_emp = SalariedEmployee(emp_id, name, monthly_salary)

    print("\n--- Salary Details ---")
    print(hourly_emp)
    print(salaried_emp)


if __name__ == "__main__":
    main()
