# Guess The Number Game
# To-Do
# 1. Main Menu
# -- A inputable "Start" and "Quit" text.
# 2. Game Loop
# -- First the console asks for a number range of guess numbers
# -- Then the user can input a number giving a range of numbers (example: 100 - Then the user guesses a number from 1 to 100)
# -- After giving the input the player can now put a random number
# -- The Console will print wether its higher or lower
# -- then that process repeats until the player gets the right number
# -- Prints how many tries the player got
# 3. Game Over Screen
# -- Asks if user wants to quit or continue playing

# Imports
from random import randint

# Variables
isGuessed = False


# Main Menu
print("Guess The Number [DEMO]")
print("Type the input to which you want to do!")
print("Start   |   Quit")
mmInput = input()

inGame = True if mmInput.lower() == "start" else False

# Game Loop
while inGame:
    isGuessed = False
    numRange = int(input("Enter a number for the range of numbers to guess: "))

    randomGuessingNum = randint(1, numRange)

    while isGuessed == False:
        guess = int(input("Enter Your Guess: "))

        if guess < randomGuessingNum:
            print("Guess Higher!")
        elif guess > randomGuessingNum:
            print("Guess Lower")
        else:
            isGuessed = True
            print("That is Correct!")
            # Restart Menu
            resMen = input("Would you like to restart? Yes | Quit : ")
            if resMen.lower() == "quit": inGame = False


# this will be a test for my new git something for real
            