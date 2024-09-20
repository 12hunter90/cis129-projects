# Coffee Shop Reciept Simulator
# Program designed to simulate the ability to purchase various coffee shop items and receive a receipt listing items
#print Decorative line to match assignment
print('*'*30)

#Print Coffee Shop Name
print("Martin's Extra Slow Coffee Shop")

#prices
coffeeprice = 5
muffinprice = 4
bagelprice = 4
espressoprice = 7
sales_tax = 0.06

#ask and receive input for number of coffees as well as muffins
Coffee = int(input('Number of coffees bought?\n'))
Muffin = int(input('Number of muffins bought?\n'))

#add input for 2 new items bagels and espresso
Bagel = int(input('Number of bagels bought?\n'))
Espresso = int(input('Number of espressos bought?\n'))

#print Decorative line to match assignment
print('*'*30)
print( )
print('*'*30)

#Calculate a subtotal
Subtotal = (Coffee * coffeeprice) + (Muffin * muffinprice)\
           + (Bagel * bagelprice) + (Espresso * espressoprice)

#Calculate sales tax
Tax = Subtotal * sales_tax

#Calculate Total Price
Total = Subtotal + Tax

#Print Coffee Shop Name
print("Martin's Extra Slow Coffee Shop Receipt")

#inform Customer of Products bought at cost per item as well as tax amount
print(f'{Coffee} Coffees at ${coffeeprice: .2f} each: $ {Coffee * coffeeprice}')
print(f'{Muffin} Muffins at ${muffinprice: .2f} each: $ {Muffin * muffinprice}')
print(f'{Bagel} Bagels at ${bagelprice: .2f} each: $ {Bagel * bagelprice}')
print(f'{Espresso} Espressos at ${espressoprice: .2f} each: $ {Espresso * espressoprice}')

#print subtotal, tax, and total
print(f'Subtotal: ${Subtotal: .2f}')
print(f'Tax: ${Tax: .2f}')
print(f'Total: ${Total: .2f}')

#print Decorative line to match assignment
print('*'*30)

#thank the customer for their business
print('Thank you for being our valued customer')

#print Decorative line to match assignment
print('*'*30)
