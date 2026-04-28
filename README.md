# python-cashier-project
A python made cashier 
Overview:
This project is a python-made cash register . It displays how many bills or coins are needed to give the best coins that can be used. 

Instructions:
To begin type your total cost . Then type how much you are giving the cashier. The cash register will tell you the best possible coins needed .  Do not use the dollar symbol , just type the amount (you are allowed to usse a decimal).

The algorithm :
The cash register takes your cost and divides by the biggest possible bil or coin ( 100 dollars). If there is no remainder the cash register displays how many are needed. If there is a remainder , the cash register goes to the next biggest possible bill or coin ($50) and divides the value of the bill of coin with how much is left. That process repeats until there is no money left ($0.00)