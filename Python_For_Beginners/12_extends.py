class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名：{self.name}\n 员工ID: {self.id}")

    def calculate_grade(self):
        print("default")
        return 0

class FUllTimeEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.monthly_salary = 0

    def set_monthly_salary(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_grade(self):
        print("我是全职员工")
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.daily_salary = 0
        self.work_days = 0

    def set_daily_salary(self, daily_salary):
        self.daily_salary = daily_salary

    def set_work_days(self, work_days):
        self.work_days = work_days

    def calculate_grade(self):
        print("我是兼职员工")
        return self.daily_salary * self.work_days

cyb = FUllTimeEmployee("cyb", 1)
cyb.set_monthly_salary(10000)
xy = PartTimeEmployee("xy", 2)
xy.set_daily_salary(200)
xy.set_work_days(22)


cyb.print_info()
cyb_monthly_salary = cyb.calculate_grade()
print(f"月薪为：{cyb_monthly_salary}")
print("\n")
xy.print_info()
xy_monthly_salary = xy.calculate_grade()
print(f"月薪为：{xy_monthly_salary}")