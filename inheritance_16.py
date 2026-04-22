class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def print_info(self):
        print(f"员工姓名:{self.name}, 工号:{self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days
        
Tom = FullTimeEmployee("Tom", "01", 7000)
David = PartTimeEmployee("David", "02", 150, 20)

Tom.print_info()
print(Tom.calculate_monthly_pay())
David.print_info()
print(David.calculate_monthly_pay())