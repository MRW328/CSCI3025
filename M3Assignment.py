#Matthew Williams
#CSCI3025

import random 

def main():
    print("Welcome to the Number Guessing Game, where I pick a number and you guess what it is!")
    
    isUserPlaying() #a method that determines if user is playing
    
    winningNumber = random.randint(1,10) #generate a number 1-10    

    guessList = [] #list for user guesses

    #while loop
    guessed = False 
    while(not guessed):

        userGuess = input("Guess a number 1-10: ")
        
        #data validation
        if not userGuess.isdigit(): #check if input is a number
            print("That is not a number")
            continue #control demonstration
        
        userGuess = int(userGuess) #cast str input into int
        
        if userGuess < 1 or userGuess > 10:
            print("your guess is out of the number range")
            continue #control demonstration

        #conditionals comparing numbers    
        if userGuess < winningNumber:
            print("Guess Higher")
        elif userGuess > winningNumber:
            print("Guess Lower")
        elif userGuess == winningNumber:
            print(f"Correct! The winning number is {winningNumber}. You Win!")
            guessed = True

        guessList.append(userGuess) #add user's guess to list   
    
    #for loop to print list of user guesses
    print("Your guesses: ")
    for x in guessList:
        print(x, end=" ")

#method to determine if user wants to play
def isUserPlaying():
    print("\nWould you like to play?")    
        
    while True:    
        userPlaying = input('Choose by selecting a number:\n1 Yes \n2 No\n')

        if userPlaying == '1':
            print("Alrighty! Let's play!") 
            break
        elif userPlaying == '2':
            print("Goodbye!") 
            exit() 
        else:
            print("Invalid Input. Try again.") 

if __name__ == "__main__":
    main()