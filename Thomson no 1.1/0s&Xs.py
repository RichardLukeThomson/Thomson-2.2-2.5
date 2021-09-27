# A noughts and crosses board (Queen's English)
# Additional lab set by Chris H
# Practicing using two-dimensional arrays (a matrix)

# Created by Thomson on 27 Sep 21

# define an empty list
tttBoard = []

# use a for loop to print a list of three underscores (row), three times resulting in a 3x3 board (tttBoard)
print("empty board:\n")
for i in range(3):
    row = ["_" for i in range(3)]
    print(row)
    tttBoard.append(row)

# insert an x in the centre and an "o" in the bottom right by using the list indexes
# The first index is the row number (the list), the second number is the column number (the element in the list)
tttBoard[1][1] = "x"
tttBoard[2][2] = "o"

# print each row separatley. The index number refers to the list within
print("\n\nammended board:\n")
for i in range(3):
    print(tttBoard[i])