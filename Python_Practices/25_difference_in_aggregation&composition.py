# Video 28

# Difference between Aggregation and Composition ---->

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary=salary

    def total_salary(self):
        return self.obj_salary.annual_salary()


salary = Salary(15000, 10000)                 # 1. creating salary class object
emp = Employee("Bishal",27,salary)            # 2. Pass the object in employee class method
print("The Total salary is: ",emp.total_salary()) 