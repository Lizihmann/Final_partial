"""
Objective. Algorithm to calculate the salary of “n” salespeople.
Each salary is made up of a base salary and a sales commission.

            Total Salary = Base salary + sales commission

The sales commission is calculated by taking a percentage of the sales made, according to the following table:

Sales	Commission percentage
Less than 3,500: 7%
3,500 – 7,000: 10%
Greater than 7000: 15%

The algorithm must ask as input: if there is another seller (yes/no response), the name of each seller, the base salary of each one and the total sales made per seller. Tip: use the lower function to validate yes and no

The output must have the seller's name and their total salary
"""

total_salary = 0
sales_comission = int(input("How many sales have been made? Give me the percentage of sales made: "))

if sales_comission < 3500:
    sales_comission = sales_comission * 7 / 100
elif sales_comission > 3500 and sales_comission < 7000:
    sales_comission = sales_comission * 10 / 100
else:
    sales_comission = sales_comission * 15 / 100

total_salary = sales_comission + 3500
print(f"The salary of the salesperson is {total_salary}")


while True: 
  another_seller = input("Do you have another sales person? (yes or no): ")
  if another_seller == "yes":
    name = input("What is the name of the salesperson?")
    base_salary = int(input("What is the base salary of that person?"))
    sales_made = int(input("How many sales have been made? Give me the percentage of sales made: "))
    if sales_made < 3500: 
      sales_made = sales_made *7/10
    elif sales_made > 3500 and sales_made < 7000: 
      sales_made = sales_made *10/10
    elif sales_made > 7000:
      sales_made = sales_made *15/10

total_salary = sales_made + base_salary
print(f"The salary of the salesperson is {total_salary}")
