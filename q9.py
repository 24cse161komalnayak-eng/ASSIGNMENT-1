class Products:
    def input(self):
        self.product_no = input("Enter the Product No: ")
        self.product_name = input("Enter the Product Name: ")
        self.cost = int(input("Enter the Cost: "))
        self.quantity = int(input("Enter the Quantity: "))

    def calculator(self):
        self.total_amount = self.cost * self.quantity

    def display(self):
        print("Product No      :", self.product_no)
        print("Product Name    :", self.product_name)
        print("Cost            :", self.cost)
        print("Quantity        :", self.quantity)
        print("Total Amount    :", self.total_amount)
        
product_list = []

for i in range(5):
    print(f"\nEnter Details of Product {i+1}")
    p = Products()
    p.input()
    p.calculator()
    product_list.append(p)

highest = product_list[0]

for i in product_list:
    if i.total_amount > highest.total_amount:
        highest = i

print("\nProduct with Highest Total Amount")
highest.display()
