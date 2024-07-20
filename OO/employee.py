class Employee:
    def __init__(self, name, job_title, annual_salary):
        self._name = name
        self._job_title = job_title
        self._annual_salary = annual_salary
        
    
    # Getter and setter for name
    def get_name(self):
        return self._name
    
    
    def set_name(self, name):
        self._name = name
        
        
    # Getter and setter for job_title
    def get_job_title(self):
        return self._job_title
    
    
    def set_job_title(self, job_title):
        self._job_title = job_title
        
        
    # Getter and setter for annual_salary
    def get_annual_salary(self):
        return self._annual_salary
    

    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary
        
        
class Company:
    def __init__(self):
        self._employees = []
        
    
    def add_employee(self, employee):
        return self._employees.append(employee)
    
    
    def calculate_total_salary(self):
        total_salary = sum(employee.get_annual_salary() for employee in self._employees)
        
        return total_salary

if __name__ == '__main__':
    # Create employees
    emp1 = Employee('John', 'Backend Developer', 5000)
    emp2 = Employee('Jane', 'Frontend Developer', 3000)
    emp3 = Employee('Jane', 'Mobile Developer', 4000)
            
    # Create company and add the employees to it
    company = Company()
    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    
    print(f'The total salary of all employees in the company is ${company.calculate_total_salary()}')
    