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
    hourly_emp = HourlyEmployee(101, "Alice", hourly_rate=20, hours_worked=160)
    salaried_emp = SalariedEmployee(102, "Bob", monthly_salary=5000)

    print(f"{hourly_emp.name}'s salary: ${hourly_emp.calculate_salary()}")
    print(f"{salaried_emp.name}'s salary: ${salaried_emp.calculate_salary()}")



 