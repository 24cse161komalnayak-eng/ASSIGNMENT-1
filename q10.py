class Employee:
    def __init__(self):
        self.emp_id = int(input("enter the id: "))
        self.emp_name = input("enter the name: ")
        self.basic_pay = int(input("enter the basic-Pay: "))
        self.ta = int(input("enter the ta: "))
        self.da = int(input("enter the da: "))

    def calc(self):
        self.gross_pay = self.basic_pay + (0.10 * self.ta) + (0.40 * self.da)

    def display(self):
        print("Emp details:")
        print("emp_id - ", self.emp_id)
        print("emp_name - ", self.emp_name)
        print("basic-Pay - ", self.basic_pay)
        print("ta - ", self.ta)
        print("da - ", self.da)
        print("gross-Pay - ", self.gross_pay)

emp = Employee()
emp.calc()
emp.display()
