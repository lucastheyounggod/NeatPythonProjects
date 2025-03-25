import getpass

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self._salary = salary
        self.department = department

    def calculate_bonus(self):
        """Base bonus calculatiion (to be overridden)"""
        return self._salary * 0.05

    def display_info(self):
        print(f"Employee: {self.name}, Department: {self.department}, Salary: {self._salary}")


class Manager(Employee):
    def calculate_bonus(self):
        return self._salary * 0.1

class Developer(Employee):
    def calculate_bonus(self):
        return self._salary * 0.07

class Intern(Employee):
    def calculate_bonus(self):
        return 500

class HRSystem:
    def __init__(self):
        self.employees = []
        self.__admin_password = "admin123"

    def authenticate(self):
        """Password authentication for admin actions"""
        password = getpass.getpass("Enter admin password: ")
        if password == self.__admin_password:
            print("Access granted!")
            return True
        else:
            print("Incorrect password. Access denied!")
            return False

    def add_employee(self, employee):
        if self.authenticate():
            self.employees.append(employee)
            print(f"{employee.name} has been added.")

    def remove_employee(self, name):
        if self. authenticate():
            for emp in self.employees:
                if emp.name == name:
                    self.employees.remove(emp)
                    print(f"name has been removed.")
                    return
            print("Employee not found.")

    def display_employees(self):
        print("\nEmployee List: ")
        for emp in self.employees:
            emp.display_info()
            print(f"Bonus: ${emp.calculate_bonus()}")
        print("_" * 30)