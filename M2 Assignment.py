#Matthew Williams
#CSCI3025

#########################
# Operations on numbers #
#########################
numOne = 5
numTwo = 9
numThree = 6

#adding 9 and 6
print(f"The sum of {numTwo} and {numThree} is {numTwo + numThree}.")
#multiplying 5 and 9
print(f"The product of {numOne} and {numTwo} is {numOne * numTwo}.")
#dividing 9 by 5
print(f"The quotient of {numTwo} and {numOne} is {numTwo / numOne}.")
#subtracting 6 from 9
print(f"The difference between {numTwo} and {numThree} is {numTwo - numThree}")



#######################
# String manipulation #
#######################

myName = 'XmatthewXwilliamsX'
#slicing
firstName = myName[1:8]
lastName = myName[9:17]
#new line
#concatenation and formatting
print("\nMy name is " + firstName.title() + " " + lastName.title() + ".")
print("The last letter of my first name is "+ firstName.upper()[-1] + ".")



############
# Booleans #
############

#new line
#5 == 9
print(f"\nIs {numOne} equal to {numTwo}? {numOne == numTwo}")
#6 > 5
print(f"Is {numThree} greater than {numOne}? {numThree > numOne}")
# 9 <= 6
print(f"Is {numTwo} less than or equal to {numThree}? {numTwo <= numThree}")