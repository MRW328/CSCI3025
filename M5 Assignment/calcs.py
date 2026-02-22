import math
import datetime

SALES_TAX = .08875

def sumTotal(cart): #not used in program
    """sums up the pre-tax total value from cart

    Returns:
        sum of cart values
    """
    return sum(cart.values())

def applyTax(cart):
    """sums up the total values from the cart dictionary with tax
    Parameters:
        cart: cart dictionary 

    Returns:
        float: sum of values from cart with SALES_TAX added
    """
    total = math.fsum(cart.values())
    
    return total + (total * SALES_TAX)

def checkBudget(total, budget):
    """returns how much is left in specified budget

    Parameters:
        total: sum of cart values
        budget: user specified parameter

    Returns:
        float: total value in cart - specified budget
    """
    
    return budget-total

def reciept(cart):
    """Creates and prints a receipt of user's cart with total

    Parameter:
        cart: cart dictionary 
    """
    print("Thank You!")
    print(datetime.datetime.now())

    for name, price in cart.items():

        print(f"{name}: ${price:.2f}")
    
    print(f"Tax: {SALES_TAX:.3%}")

    print(f"Total: ${applyTax(cart):.2f}")