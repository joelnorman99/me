"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    actual_number = False
    
    while not actual_number:
        guess = str(input(message))
        if guess.isdigit():
            actual_number = True
            return int(guess)
        else:
            print("Not a number")



def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    lowerBound = not_number_rejector("Enter Lower Bound: ")

    higher_number = False  #we need to set an upper and lowerbound for game

    while not higher_number:
      upperBound = not_number_rejector("Enter Upper Bound: ")
      if upperBound > lowerBound:
        higher_number = True
      else:
        print("The upperbound is lower than you lowerbound: TRY AGAIN")
        
      #above code ensures upper > lower, see stubbon_asker in EX1 
    
    print("OK then, guess a number between {} and {} ?".format(lowerBound,upperBound))
    lowerBound = int(lowerBound) #ensures integer is give (Not a letter)
    upperBound = int(lowerBound) 

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("HOW DID YOU GET THAT! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Guess is too small, try again ".format(actualNumber))
        else:
            print("Guess is too big, try again ".format(actualNumber))
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!



if __name__ == "__main__":
    print(advancedGuessingGame())
