"""
Algorithm for obtaining zoo statistics.
Create an algorithm to obtain statistics in a zoo where a count and percentage of “n” animals within a certain age range is required:

Less than 2 years
Between 2 and less than 5 years
Between 5 and less than 10 years
Greater than or equal to 10 years

The diagram should ask as input: if there is another animal to be recorded (yes/no response), the age (years) of each one. Tip: use the lower function to validate yes and no

The output must specify the number and percentage of animals in each age range.
"""

animals = []
while True: 
  animal = input("Do you have another animal? Yes/No: ")
  if animal == "yes": 
    age = int(input("What is the age of the animal: "))
    animals.append(age)

if age < 2: 
  print("Less than 2 years")
elif age < 5: 
  print("Between 2 and 5 years")
elif age < 10: 
  print("Between 5 and 10 years")

age_range_percentage = animals.count(age) / len(animals) *100
print(f"The percentage of animals in each age group is {age_range_percentage}%")
print(f"The number of animals in each age group is {animals.count(age)}")
