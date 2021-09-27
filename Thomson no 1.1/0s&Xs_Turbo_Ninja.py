# A " turbo ninja" noughts and crosses game (Queen's English)
# Additional lab set by Chris H with my own improvements
# Practicing using two-dimensional arrays (a matrix)

# Created by Thomson on 27 Sep 21

# This has the following improvements on TTT_ninja.py
# - You cannot cheat and overwrite a previosly written value
# - the game ends when somebody wins
# the user can still input values that will cause a runtime error. Need to learn about input validation.

# define an empty list
tttBoard = []

# use a for loop to create a list of three underscores (row), three times resulting in a 3x3 board (tttBoard)
for i in range(3):
    row = ["_" for i in range(3)]
    tttBoard.append(row)

# declare a variable which will be used later
game_won = 0

# create an infinite while loop that checks the value of input_symbol. If the user types q, the while loop ends.
while game_won == 0:

    #prompt the user for input and store it in variables (this bit needs input validation)
    input_row = int(input("Enter a row (0 to 2):  "))
    input_column = int(input ("Enter column (0 to 2):  "))

    # check the row and column number to see if it has been used before. If so rebuke the player and go back to the top.
    if tttBoard[input_row][input_column] == "x" or tttBoard[input_row][input_column] == "o":
        print("\nSTOP CHEATING, THAT SPACE IS TAKEN!!! Pick another row and column\n")
        continue
    
    # prompt the user to enter an o or x, this bit needs input validation
    input_symbol = input ("Enter o or x, or q to quit:  ")
    if input_symbol == "q":
        break

    # update the values in the list using the user's input
    tttBoard[input_row][input_column] = input_symbol

    #print each row separatley
    print("\n",tttBoard[0],sep="")
    print(tttBoard[1])
    print(tttBoard[2],"\n")
    
    # this section detects if the game has been won. It could definitley be shortened!
    for i in range(3):
        # detect any winning rows
        winner_x = ["x" for j in range(3)]
        winner_o = ["o" for j in range(3)]
        if tttBoard[i] == winner_x:
            game_won = 1
        if tttBoard[i] == winner_o:
            game_won = 2
        
        # detect any winning columns
        for j in range(3):
            if tttBoard[0][i] == "x" and tttBoard[1][i] == "x" and tttBoard[2][i] == "x":
                game_won = 1
        for j in range(3):
            if tttBoard[0][i] == "o" and tttBoard[1][i] == "o" and tttBoard[2][i] == "o":
                game_won = 2

    # detect any winning diagonals (i'm not too proud of this bit, there must be a better way)
    if tttBoard[0][0] == "x" and tttBoard[1][1] == "x" and tttBoard[2][2] == "x":
        game_won = 1
    if tttBoard[0][0] == "o" and tttBoard[1][1] == "o" and tttBoard[2][2] == "o":
        game_won = 2
    if tttBoard[0][2] == "x" and tttBoard[1][1] == "x" and tttBoard[2][0] == "x":
        game_won = 1
    if tttBoard[0][2] == "o" and tttBoard[1][1] == "o" and tttBoard[2][0] == "o":
        game_won = 2

    # check the value of game_won. If changed, a message will be displayed and the while loop will end.
    if game_won == 1:
        print("\nWe have a winner, well done x's!\n")
    if game_won == 2:
        print("\nWe have a winner, well done o's!\n")