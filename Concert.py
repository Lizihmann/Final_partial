https://replit.com/join/paadiijynp-liz-sophiesophi
"""
Concert ticket algorithm.
Objective: Create an algorithm to calculate the cost of tickets for a concert for "n" attendees.
Calculate the total cost considering the following:

Cost per seat: Zone 1 - $2000, Zone 2 - $1000, Zone 3 - $700
Complimentary coupons per person: Platinum $500, Gold $300, Silver $200
Note 1: These coupons are valid only from Monday to Thursday.

The algorithm should request the following input: customer name, zone, day of the week, and the type of coupon for each attendee (if they have a coupon).
Note 2: The loop will end if there are no more customers to attend, so ask if there is another customer in line.

The output should include:
The name of the attendee and the total cost
The algorithm should also accumulate the total sales of the "n" tickets and report the result at the end.
"""
attendees = 0
total_cost = 0
name = input("What's your name?")
seat = input("What seat do you want? Options: Zone 1, Zone 2, Zone 3: ")
complimentary_coupons = input("Do you have any complimentary coupons? Options: Platinum, Gold, Silver")
day_of_week = input("What day of the week is it? Options: Monday, Tuesday")
attendees = int(input("How many attendees are there?"))

attendees = cost + seats + complimentary_coupons

if day_of_week == "Monday" or "Tuesday":
  print("Your ticket works!")
  
if seat == "Zone 1":
    cost = 2000
elif seat =="Zone 2":
    cost = 1000
elif seat =="Zone 3":
    cost = 700

if complimentary_coupons == "Platinum":
  complimentary_coupons = 500

elif complimentary_coupons == "Gold":
  complimentary_coupons = 300
elif complimentary_coupons == "Silver":
  complimentary_coupons = 200

total_cost = cost + complimentary_coupons

print(f"The total cost of your ticket is: ${total_cost}") 

print("The complimentary coupons are: ", complimentary_coupons)

