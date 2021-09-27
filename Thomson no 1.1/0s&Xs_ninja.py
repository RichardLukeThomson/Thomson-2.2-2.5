# A " ninja" noughts and crosses game (Queen's English)
# Additional lab set by Chris H
# Practicing using two-dimensional arrays (a matrix)

# Created by Thomson on 27 Sep 21

# define an empty list
tttBoard = []

# use a for loop to create a list of three underscores (row), three times resulting in a 3x3 board (tttBoard)
for i in range(3):
    row = ["_" for i in range(3)]
    tttBoard.append(row)

# declare a variable which will be used later
input_symbol = "anything"

# create an infinite while loop that checks the value of input_symbol. If the user types q, the while loop ends.
while input_symbol != "q":

    #prompt the user for input and store it in variables
    input_row = int(input("Enter row: "))
    input_column = int(input ("Enter column: "))
    input_symbol = input ("Enter o or x, or q to quit")

    # update the values in the list using the user's input
    tttBoard[input_row][input_column] = input_symbol

    #print each row separatley
    print(tttBoard[0])
    print(tttBoard[1])
    print(tttBoard[2])

# a few limitations of this are:
# - the user can input values that will cause a runtime error
# - you can overwrite a previously written value (cheating!)
# - there's no end defined, nothing happens if you win