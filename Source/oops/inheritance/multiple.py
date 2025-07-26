class Employee:
    def work(self):
        print("Working on office tasks.")

    def display(self):
        print("Employee")

class Driver:
    def drive(self):
        print("Driving the company vehicle.")
    def display(self):
        print("Driver")

class DriverEmployee(Employee, Driver):
    def report(self):
        print("Reporting both work and driving status.")

john = DriverEmployee()
john.work()      # From Employee
john.drive()     # From Driver
john.report()    # Own method
john.display()