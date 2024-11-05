#Sejiro K
#10/11/24
#P2HW2
#Grade Calculator

"""

"""

print("\nGrade Calculator \n\n")

#Initializing important variables
grades = []
i = 1
gradeCount = int(input("How many grades do you want to enter? "))
print()


#Loop de-loop
for i in range(0, gradeCount):
    grade = float(input(f"Input grade {i + 1}: "))
    
    while grade < 0 or grade > 100:
        grade = float(input("\nGrades must be between 0 and 100. Please re-enter grade: "))

    grades.append(grade)


#List modification
lowest = min(grades)
grades.remove(lowest)


#Letter calculation
average = sum(grades) / len(grades)
finalGrade = ""

if average >= 90:
    finalGrade = "A"
    
elif average >= 80:
    finalGrade = "B"

elif average >= 70:
    finalGrade = "C"

elif average >= 60:
    finalGrade = "D"

else:
    finalGrade = "F"


#Le Results
print("\nResults: \n")

print(f"Lowest Grade: {min(grades)}")
print(f"Highest Grade: {max(grades)}")
print(f"Total Grade: {sum(grades)}")
print(f"Modified List: {grades}")
print(f"Average Grade: {average}")
print(f"Final Grade: {finalGrade}")
