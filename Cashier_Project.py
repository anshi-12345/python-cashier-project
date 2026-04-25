import sys
user_cash = int(input("What is the cost of your item? "))

user_spent = int(input("How much are you giving to spend? "))

if user_spent < user_cash:
    print("Not enough money. Sorry you can't purchase this item. BYEEEE")
    sys.exit()

change = user_spent - user_cash

if change >= 100 :
    bills_100 = change//100
    change = change - bills_100 *  100
    print( str(bills_100)  + " 100 dollar bill(s)")

elif change >= 50:
    bill_50 = change//50
    change = change - bill_50 * 50
    print(str(bill_50) + " 50 dollar(s) bills")
