name = input('enter your name ! ')
product = float(input('enter the price of any product !'))
discount = product * 5 / 100
newprice = product - discount

print(f'hello {name} the discount of 5 % of  the product is {discount:.2f}\nand the new price is {newprice:.2f}')