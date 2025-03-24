from abc import ABC, abstractmethod

# Define the abstract Employee class
class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass  # This method will be overridden by subclasses

# Define the HourlyEmployee subclass
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary=0)  # Base salary is not used
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

# Define the SalariedEmployee subclass
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, salary=monthly_salary)

    def calculate_salary(self):
        return self.salary  # Monthly salary remains the same

# Example usage: create an input parameter
if __name__ == "__main__":
    hourly_emp = HourlyEmployee(101, "kiss", hourly_rate=20, hours_worked=160)
    salaried_emp = SalariedEmployee(102, "Bob", monthly_salary=5000)

    print(f"{hourly_emp.name}'s salary: ${hourly_emp.calculate_salary()}")
    print(f"{salaried_emp.name}'s salary: ${salaried_emp.calculate_salary()}")







   
