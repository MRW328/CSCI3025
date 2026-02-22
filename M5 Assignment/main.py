#Matthew Williams
#CSCI3025


import calcs
from groceryCart import addToCart, removeFromCart, displayCart, cart 

addToCart("Beans", 5.44)
addToCart("Milk", 3.49)
addToCart("Bread", 2.99)
addToCart("Better Beans", 4.99)

removeFromCart("Beans")

displayCart()
calcs.reciept(cart)

print(f"Budget remaining: ${calcs.checkBudget(calcs.applyTax(cart), 20.00):.2f}") #check cost against $20 budget