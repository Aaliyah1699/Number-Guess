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
'''1st if statement -> if answer yes - print reply and then exit() else call 1st function name w/ ()'''
