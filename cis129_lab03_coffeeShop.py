# Coffee Shop Reciept Simulator
#print Decorative line to match assignment
print('*'*30)

#Print Coffee Shop Name
print("Martin's Extra Slow Coffee Shop")

#prices
coffeeprice = 5
muffinprice = 4
sales_tax = 0.06

#ask and receive input for number of coffees as well as muffins
Coffee = int(input('Number of coffees bought?\n'))
Muffin = int(input('Number of muffins bought?\n'))
#print Decorative line to match assignment
print('*'*30)
print( )
print('*'*30)
#Calculate a subtotal
Subtotal = (Coffee * coffeeprice) + (Muffin * muffinprice)

#Calculate sales tax
Tax = Subtotal * sales_tax

#Calculate Total Price
Total = Subtotal + Tax

#Print Coffee Shop Name
print("Martin's Extra Slow Coffee Shop")

#inform Customer of Products bought at cost per item as well as tax amount
print(f'{Coffee} Coffees at ${coffeeprice: .2f} each: $ {Coffee * coffeeprice}')
print(f'{Muffin} Muffins at ${muffinprice: .2f} each: $ {Muffin * muffinprice}')

#print subtotal, tax, and total
print(f'Subtotal: ${Subtotal: .2f}')
print(f'Tax: {Tax: .2f}')
print(f'Total: {Total: .2f}')

#print Decorative line to match assignment
print('*'*30)
