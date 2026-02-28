
class  Employee: # Class to represent an employee in the Employee Management System
    def __init__(self, emp_id, name, department, basic_salary, experience):  # Single constructor to initialize employee attributes
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.experience = experience

    def calculate_annual_salary(self): # Method to calculates and returns the annual salary based on the basic salary
        annual_salary = self.basic_salary * 12
        return annual_salary
    
    def apply_increment(self, increment_percent): # Method to updates the employee’s basic_salary after applying the increment percentage and returns the new basic salary
        increment_amount = self.basic_salary * (increment_percent / 100)
        self.basic_salary += increment_amount
        return self.basic_salary
    
    def add_experience(self, years): # Method to add years of experience to the employee's current experience
        self.experience += years
        return self.experience
    
    def change_department(self, new_department): # Method to change the employee's department
        self.department = new_department
        return self.department
    
    def  get_employee_summary(self): # Method to get a summary of the employee's details
        summary = f"Employee ID: {self.emp_id}\nName: {self.name}\nDepartment: {self.department}\nBasic Salary: {self.basic_salary}\nExperience: {self.experience} years"
        return summary # Method to return a formatted string containing the employee's details

# Calling the Employee class and its methods   
Employee1 = Employee(101, "Virendra", "IT", 50000, 5)
add_experience = Employee1.add_experience(2)
apply_increment = Employee1.apply_increment(30)
change_department = Employee1.change_department("Sr.IT")
calculate_annual_salary = Employee1.calculate_annual_salary()
employee_summary = Employee1.get_employee_summary()
print(f"Updated Employee Summary: \n{employee_summary}")