# Sejiro K.
# 11/5/24
# P4HW2
# Calculate and print employee salary


#Important Variables
employeeCount = 0
totalRegularPay = 0
totalOvertimePay = 0
totalGrossPay = 0

print("Employee Pay Receipt\n")

running = input("Would you like to run this program? (yes/no): ") #I added this for the funnies
print()

#Logic
while running == "yes":
    
    name = input("\nEnter Employee name: ")
    hours = float(input(f"Enter {name}'s hours worked: "))
    wage = float(input(f"Enter {name}'s wage: "))
    print()

    if hours > 40:
        overtime = hours - 40
    else:
        overtime = 0

    regularPay = (hours - overtime) * wage
    overtimePay = overtime * wage * 1.5
    totalPay = regularPay + overtimePay

    #Stuff
    print("Employee name: " + name)

    print("Hours Worked     Wage     Overtime Hours     Regular Pay     Overtime Pay     Total Pay")
    print("------------------------------------------------------------------------------------------")
    print(f"{hours:<16} {wage:<8} {overtime:<18} ${regularPay:<14.2f} ${overtimePay:<15.2f} ${totalPay:<16.2f}")

    #More stuff
    employeeCount += 1
    totalRegularPay += regularPay
    totalOvertimePay += overtimePay
    totalGrossPay += totalPay
    
    running = input("\nDo you want to run the calculator again? ")


#Finale
print("Final Results: \n")
print(f"Total Employees: {employeeCount}")
print(f"Total Regular Pay: {totalRegularPay:.2f}")
print(f"Total Overtime Pay: {totalOvertimePay:.2f}")
print(f"Total Gross Pay: {totalGrossPay:.2f}")
