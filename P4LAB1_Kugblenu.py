#Sejiro Kugblenu
#10/31/24
#P4LAB2
#Times Tables

running = "yes"

while running == "yes":

    num = int(input("\nEnter and integer: "))
    print()

    if num >= 0 :
        
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
            i += 1

    else:
        
        print("This program only accepts positive integers")

    running = input("\nDo you want to run this program again? (yes/no): ")

print("\nThis program is over")
