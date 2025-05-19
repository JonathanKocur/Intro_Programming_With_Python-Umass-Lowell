# Jonathan Kocur
# 2/13/23
# Assignment 3

# This program simulates a simple game called "Mastermind" where the computer generates a random 
# color sequence, and the user had to guess in a specified number of tries.The program will show 
# the user the accuracy of their guess, and print messages if the guess invalid.


# This part of the code generates a random sequence of 4 letters, each representing
# a color specified in the legal_colors list 
legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']

def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

# Here the instruction messages are printed for the user when they are making their guesses.
# The user must pick from the possible colors (not case sensative) and not repeat them.
print ("Possible colors are R, G, B, Y, W, O, M, V")
print ("Please enter your guess with no spaces between colors. Colors cannot be repeated")
game = True
attempts = 0

# This part is a while loop that operates each turn of the game. Each iteration represents a turn,
# Which takes user input and runs through a series of tests to analyze the user input's accuracy.
while game == True:
    attempts = attempts + 1
    error = False
    print ("Guess ",attempts,": ",end="")
    player_guess = input().upper()

	# This section is the error check of the while loop. The first if statement checks if the user
	# input is the correct length, if not, it prints a message and moves to the next interation.
	# The for loop scans through the user guess to see if colors are repeated or if they are valid.
    if attempts < 5 and len(player_guess) != len(colors):
        print ("The user input must be exactly 4 colors")
        continue
    elif attempts == 5 and len(player_guess) != len(colors):
        print("You lose!")
        break

    for i in range(4):
        if attempts < 5 and player_guess[i] not in legal_colors:
            print (player_guess[i],"is not a valid color, try again")
            error = True
        elif attempts == 5 and player_guess[i] not in legal_colors:
            error = True
    for i in range(4):
        if attempts < 5 and i >= 1 and player_guess[i] == player_guess[i-1]:
            print ("Colors cannot be repeated, try again")
            error = True
        elif (attempts == 5) and (player_guess[i] == player_guess[i-1]):
            error = True


    if error == True and attempts == 5:
        print("You lose!")
        break
    elif error == True and attempts < 5:
        continue

	# This for loop represents the correction statement of each user guess. If a certain element
	# of the color sequence equals the same element of the guess, an empty array is assigned "R",
	# if not it is assigned "W" or "_". Then it is printed to show the user's accuracy for the turn.
    correction = ["","","",""]
    for i in range(len(colors)):
        if player_guess[i] == colors[i]:
            correction[i] = "R"
        if player_guess[i] != colors[i] and player_guess[i] in colors:
            correction[i] = "W"
        if player_guess[i] != colors[i] and player_guess[i] not in colors:
            correction[i] = "_"

    print(str(correction[0])+str(correction[1])+str(correction[2])+str(correction[3]))

	# These if statements check if the user has won or not. If correction array has all "R"s, the game
	# prints a win message and the loop is broken ending the game. If the correction array does not
	# all "R"s and it is the final turn, a losing message is printed and the game ends.
    if correction != ["R","R","R","R"] and attempts == 5:
        print ("You lose!")
        break
    if correction == ["R","R","R","R"]:
        print ("You win!")
        break





