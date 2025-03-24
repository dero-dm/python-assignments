class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        salary = hourly_rate * hours_worked  # Calculate salary
        super().__init__(emp_id, name, salary)  # Pass calculated salary to parent class
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)  # Correctly call parent constructor

    def calculate_salary(self):
        return self.salary

if __name__ == "__main__":
    # Get input for Hourly Employee
    print("Enter details for Hourly Employee:")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    hourly_rate = float(input("Enter Hourly Rate: "))
    hours_worked = float(input("Enter Hours Worked: "))
    
    hourly_emp = HourlyEmployee(emp_id, name, hourly_rate, hours_worked)

    # Get input for Salaried Employee
    print("\nEnter details for Salaried Employee:")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    monthly_salary = float(input("Enter Monthly Salary: "))

    salaried_emp = SalariedEmployee(emp_id, name, monthly_salary)

    # Display salaries
    print(f"\n{hourly_emp.name}'s salary: ${hourly_emp.calculate_salary():.2f}")
    print(f"{salaried_emp.name}'s salary: ${salaried_emp.calculate_salary():.2f}")
