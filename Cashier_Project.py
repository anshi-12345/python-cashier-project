import sys
user_cash = float(input("What is the cost of your item (s)? "))

user_spent = float(input("How much are you giving to spend? "))

if user_spent < user_cash:
    print("Not enough money. Sorry you can't purchase this item. BYEEEE")
    sys.exit()

change = user_spent - user_cash

if change >= 100 :90
bills_100 = change//100
change = change - bills_100 *  100
print( str(bills_100)  + " 100 dollar bill(s)")

if change >= 50:
    bill_50 = change//50
    change = change - bill_50 * 50
    print(str(bill_50) + " 50 dollar(s) bills")

if change >= 20:
    bill_20 = change//20
    change = change - bill_20 * 20
    print(str(bill_20) + " 20 dollar(s) bills")

if change >= 10:
    bill_10 = change//10
    change = change - bill_10 * 10
    print(str(bill_10) + " 10 dollar(s) bills")

if change >= 5:
    bill_5 = change//5
    change = change - bill_5 * 5
    print(str(bill_5) + " 5 dollar(s) bills")

if change >= 2:
    bill_2 = change//2
    change = change - bill_2 * 2
    print(str(bill_2) + " 2 dollar(s) bills")

if change >= 1:
    bill_1 = change//1
    change = change - bill_1 * 1
    print(str(bill_1) + " 1 dollar(s) bills")

if change >= 0.25:
    quarters = change//0.25
    change = change - quarters * 0.25
    print(str(quarters) + " 0.25 cent quarter (s)")

if change >= 0.10:
    dimes = change//0.10
    change = change - dimes * 0.10
    print(str(dimes) + " 0.10 dime(s)")

if change >= 0.05:
    nickels = change//0.05
    change = change - nickels * 0.05
    print(str(nickels) + " 0.05 nickel(s)")
