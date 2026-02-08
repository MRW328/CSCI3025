#Matthew Williams
#CSCI3025
# This program runs a simulation of the Monty Hall show.
# The user is prompted if they want to play a game.
# The user picks 1 of 3 doors and chooses to switch a door

import random #random used to generate a random winning door each time the game is played
import time #time is used to simulate program processing with the sleep() method

print('Welcome to the Monty Hall game show!\n')

def playing():
    playing = True
    while(playing):    
    
        isPlaying = input('Are you ready to play?\nChoose by selecting a number:\n1 Yes \n2 No\n')

        if isPlaying == '1':
            print("Alrighty! Let's play!") #I learned about single quote strings and apostrophes
            return 1
        elif isPlaying == '2':
            print("Alrighty, see you next time!") 
            break
        else:
            print("We'll take that as a 'no'! Good bye!") 
            break
    return 0

def generatePrizeDoor():
    return random.randint(1,3)  #selects a random winning door 1-3 

def playerDoor():
    prizeDoor = random.randint(1,3)  #selects a random winning door 1-3 
    
    #this simulates the program "processing"
    for x in range(3):
       time.sleep(.25)
       print(".", end="")

    #door selection
    invalidInput = True
    while invalidInput:

        playerDoor = input("\nSelect a door: 1  2  3\n")        
        
        #data validation 
        if playerDoor != '1' and playerDoor != '2' and playerDoor != '3':
            print("Incorrect input!, Please choose again.")
            invalidInput = True
        else: 
            invalidInput = False
    
    #program "processing"
    for x in range(3):
       time.sleep(.25)
       print(".", end="")

    print(f"\nYou've chosen door number {playerDoor}")
    
    return int(playerDoor)

def doorChange():
    playerChange = input("\nWould you like to change your door? \n1 Yes \n2 No")




if playing() <= 0:
    exit()

playerDoorInt = playerDoor()

print(playerDoorInt) 




   