"""
Sejiro K.
9/24/24
P1HW2
Program for calculating travel expenses
"""


"""
Pseudocode:
Declare Float budget, gasBudget, homeCost, foodCost
Declare String destination

Display "Input budget"
Input budget

Display "Input destination"
Input destination

Display "Input gas cost"
Input gasBudget

Display "Input home cost"
Input homeCost

Display "foodCost"
Input foodCost

Declare Float subtotal, tax, total
Set subtotal = gasBudget + homeCost + foodCost
Set tax = subtotal * 0.07
Set total = subtotal + tax
"""


print("-------Travel Budget Calculator-------")
print()

budget = input("Enter your travel budget: $")
budget = float(budget)
print()
destination = input("Enter your travel destination: ")
print()
gasBudget = input("Enter estimated gas price: $")
print()
homeCost = input("Enter estimated accomadations/home cost: $")
print()
foodCost = input("Enter estimated food cost: $")

print()
print("-------Total Prices-------")
print()

subtotal = float(gasBudget) + float(homeCost) + float(foodCost)
tax = subtotal * 0.07
totalCost = subtotal + tax

print("Destination:", destination)
print()
print(f"Estimated subtotal:   ${subtotal: .2f}\n")

print(f"Estimated tax:   ${tax: .2f}\n")

print(f"Estimated total:   ${totalCost: .2f}\n")

print(f"Estimated remaining budget:   ${budget - totalCost: .2f}")
