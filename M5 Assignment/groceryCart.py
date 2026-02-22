
cart={} #i needed curly braces

def addToCart(name, price): #adds item to cart dictionary
    """adds name and price of item to cart

    Parameters:
        name: name of item
        price: cost/value of item
    """
    
    cart[name] = price
    
def removeFromCart(name):
    """removes specified key value from cart dictionary

    parameters:
        name: name of item
    """
    del cart[name]

def displayCart(): #returns cart via dictionary\
    """displays the cart dictionary
    """
    print(cart)