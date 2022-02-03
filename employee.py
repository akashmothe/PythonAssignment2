
class Employee():
    def __init__(self, com_name, com_loc):
        self.com_name = com_name
        self.com_loc = com_loc

    def personal_details(self):
        self.emp_name = input("Enter the employee name: ")
        self.emp_email = input("Enter email: ")
        self.emp_salary = int(input("Enter the salary: "))

    def gross_salary(self):
        self.pf = (10/100)*self.emp_salary
        self.final_salary = self.emp_salary - self.pf

    def show_emp_details(self):
        print(f"Company Name is: {self.com_name}")
        print(f"Company locations is: {self.com_loc}")
        print(f"Employee name is: {self.emp_name}")
        print(f"Employee email is: {self.emp_email}")
        print(f"Employee salary is: {self.final_salary}")
    

