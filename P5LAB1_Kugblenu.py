#Sejiro K.
#11/14/24
#P5LAB1
#Modified Change Calculator

import math
import random

def selfCheck():
    
    price = round(random.uniform(0.01, 100.00), 2)

    
    print(f"Your total is ${price:.2f}\n")
    amountPaid = float(input("How much will you pay? "))

    totalChange = amountPaid - price

    if totalChange >= 0:

        print(f"You are owed ${totalChange:.2f} in change\n")

        bills = int(totalChange)


        bills_100 = bills // 100 #$100 Bills
        bills_50 = (bills - (bills_100 * 100)) // 50 #$50 Bills
        bills_20 = (bills - ((bills_100 * 100) + (bills_50 * 50))) // 20 #$20 Bills
        bills_10 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20))) // 10 #$10 Bills
        bills_5 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20) + (bills_10 * 10))) // 5 #$5 Bills
        bills_1 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20) + (bills_10 * 10) + (bills_5 * 5)))


        #There's probably a more efficent way to do this but I'm not smart enough to figure that out :)
        #Actually wait I just remebered the % operator
        #I'm not going back, if it works it works


        #Coins
        coins = (round(totalChange % 1, 2) * 100)

        quarters = coins // 25
        dimes = (coins - (quarters * 25)) // 10
        nickels = (coins - ((quarters * 25) + (dimes * 10))) // 5
        pennies = (coins - ((quarters * 25) + (dimes * 10) + (nickels * 5)))

        print("You will be given: ")
        
        print(bills_100, "$100 dollar bills")
        print(bills_50, "$50 dollar bills")
        print(bills_20, "$20 dollar bills")
        print(bills_10, "$10 dollar bills")
        print(bills_5, "$5 dollar bills")
        print(bills_1, "$1 dollar bills\n")

        print("and\n")

        print(int(quarters), "Quarters")
        print(int(dimes), "Dimes")
        print(int(nickels), "Nickels")
        print(int(pennies), "Pennies")

    else:
        print(f"You are ${totalChange * -1:.2f} short\n")



def main():
    selfCheck()

if __name__ == "__main__":
    main()
