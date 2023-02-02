'''Number Guessing  Game'''
import random
# Empty attempts list
attempts_list = []
'''1st Function to show score with -> if not / else linking to attempts list with 2 prints + print 1 No high score so user wins + print 2 f string {min(attempts)} showing the current high score'''


def show_score():
    if not attempts_list:
        print("There is no high score, you win!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


'''2nd Function to start game with attempts var, and random var = random.randint(range,nums) + print welcoming user to game and asking user for name then use f str asking {user} if they want to play'''


def game_start():
    # variable to hold the number of attempts starting at 0
    attempts = 0
    # pick a random number between 100 - 120
    ran_num = random.randint(100, 120)
    # Welcome to game statement
    print("Hey smarty pants! Welcome to the Guessing Game!")
    # Ask user their name
    name = input("What's your name? ")
    # Ask if the want to play using format to insert their name
    game_play = input(
        f"Howdy,{name}, would you like to play the guessing game (Y/N)? ")

'''1st if statement -> if answer yes - print reply and then exit() else call 1st function name w/ ()'''
   # if user says no exit game else go to score
    if game_play.lower() == 'n':
        print("All good, Thanks!")
        exit()
    else:
        show_score()
    # while yes is the answer try and guess a number
    while game_play.lower() == 'y':
        try:
            guess = int(input("Pick a number between 100 and 120: "))
            # if the guess is less than 100 or greater than 120 raise error
            if guess < 100 or guess > 120:
                raise ValueError("Please pick number in given range.")