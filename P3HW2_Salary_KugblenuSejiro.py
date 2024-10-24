# Sejiro K.
# 10/24/24
# P3HW2
# Calculate and print employee salary

print("Employee Pay Receipt\n")
name = input("Enter Employee name: ")
hours = float(input("Enter hours worked: "))
wage = float(input("Enter employee wage: "))

if hours > 40:
    overtime = hours - 40
else:
    overtime = 0

regularPay = (hours - overtime) * wage
overtimePay = overtime * wage * 1.5
totalPay = regularPay + overtimePay

print("------------------")
print("Employee name: " + name)

print("Hours Worked     Wage     Overtime Hours     Regular Pay     Overtime Pay     Total Pay")
print("------------------------------------------------------------------------------------------")
print(f"{hours:<16} {wage:<8} {overtime:<18} ${regularPay:<14.2f} ${overtimePay:<15.2f} ${totalPay:<16.2f}")
