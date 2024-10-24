#Sejiro Kugblenu
#10/17/24
#P3LAB
#Money Change Calculator

import math

print("Change Calculator\n\n")
cash = float(input("How much money would you like to exchange: "))


if cash > 0:

    #Starting with dollar bills
    bills = int(cash)


    bills_100 = bills // 100 #$100 Bills
    bills_50 = (bills - (bills_100 * 100)) // 50 #$50 Bills
    bills_20 = (bills - ((bills_100 * 100) + (bills_50 * 50))) // 20 #$20 Bills
    bills_10 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20))) // 10 #$10 Bills
    bills_5 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20) + (bills_10 * 10))) // 5 #$5 Bills
    bills_1 = (bills - ((bills_100 * 100) + (bills_50 * 50) + (bills_20 * 20) + (bills_10 * 10)))


    #There's probably a more efficent way to do this but I'm not smart enough to figure that out :)
    #Actually wait I just remebered the % operator
    #I'm not going back, if it works it works


    #Coins
    coins = (round(cash % 1, 2) * 100)

    quarters = coins // 25
    dimes = (coins - (quarters * 25)) // 10
    nickels = (coins - ((quarters * 25) + (dimes * 10))) // 5
    pennies = (coins - ((quarters * 25) + (dimes * 10) + (nickels * 5)))


    #Finally printing the answers

    print("\n\n")
    print("$", cash, "can be exchanged into: \n")


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

elif cash == 0:
    
    print("\nYou cannot make change for this")

else:
    print("\nSucks to be you lol, you're in debt 🤣")
