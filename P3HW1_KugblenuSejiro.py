# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print("\n\n")

print("Results: ")
print()

print("Lowest Grade:", low)
print("Highest Grade:", high)
print("Total Grade:", total)
print("Final Grade:", avg)

print()

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
    
elif avg < 90 and avg >= 80:
    print("Your grade is: B")

elif avg < 80 and avg >= 70:
    print("Your grade is: C")

elif avg < 70 and avg >= 60:
    print("Your grade is: D")

else:
    print("Your grade is: F")
