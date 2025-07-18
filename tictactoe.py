import random

# Creating a 2D board
renderboard = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

# Variables
currentSymbol = "+" 
whoWins = None 
isGameInProgress = True 

# function to print the game board
def drawrenderboard(renderboard):
    print(renderboard[0][0] + " | " + renderboard[0][1] + " | " + renderboard[0][2])
    print("---------")
    print(renderboard[1][0] + " | " + renderboard[1][1] + " | " + renderboard[1][2])
    print("---------")
    print(renderboard[2][0] + " | " +  renderboard[2][1] + " | " + renderboard[2][2])

def gameposition():
    print("\nWelcome to Tic Tac Toe game by Deepak Kumar or @einsstark :D")
    print("\nTo make a move, enter the rowNumber (0-2) and colNumberumn (0-2) where you want to place your mark (X).")
    print("Example: To select the middle rowNumber and rightmost colNumberumn, enter 1 for the rowNumber and 2 for the colNumberumn.\n")
    print("Refer to the position table below for reference.")
    print('''
    0,0 | 0,1 | 0,2
    ---------------
    1,0 | 1,1 | 1,2
    ---------------
    2,0 | 2,1 | 2,2\n''')
    return gameposition

# Player input
def playerInput(renderboard):
    global rowNumber, colNumber
    rowNumber = int(input("Enter the rowNumber values from (0-2): "))
    colNumber = int(input("Enter the colNumberumn values from (0-2): "))
    if 0 <= rowNumber <= 2 and 0 <= colNumber <= 2 and renderboard[rowNumber][colNumber] == ' ':
        renderboard[rowNumber][colNumber] = currentSymbol
        return True
    else:
        print("Invalid input. Try again.")
        return False

# Check for horizontal whoWins
def check_horizontal_whoWins(renderboard):
    global whoWins
    if renderboard[0][0] == renderboard[0][1] == renderboard[0][2] != ' ': 
        whoWins = renderboard[0][0]
        return True
    elif renderboard[1][0] == renderboard[1][1] == renderrenderboard[1][2] != ' ': 
        whoWins = renderboard[1][0]
        return True
    elif renderboard[2][0] == renderboard[2][1] == renderboard[2][2] != ' ':
        whoWins = renderboard[2][0]
        return True

# Check for vertical whoWins
def check_vertical_whoWins(renderboard):
    global whoWins
    if renderboard[0][0] == renderboard[1][0] == renderboard[2][0] != ' ':
        whoWins = renderboard[0][0]
        return True
    elif renderboard[0][1] == renderboard[1][1] == renderboard[2][1] != ' ':
        whoWins = renderboard[0][1]
        return True
    elif renderboard[0][2] == renderboard[1][2] == renderboard[2][2] != ' ':
        whoWins = renderboard[0][2]
        return True

# Check for diagonal whoWins
def check_diagonal_whoWins(renderboard):
    global whoWins
    if renderboard[0][0] == renderboard[1][1] == renderboard[2][2] != ' ':
        whoWins = renderboard[0][0]
        return True
    elif renderboard[0][2] == renderboard[1][1] == renderboard[2][0] != ' ':
        whoWins = renderboard[0][2]
        return True

# Check win
def check_win(): 
    global isGameInProgress
    if (check_horizontal_whoWins(renderboard) or 
        check_vertical_whoWins(renderboard) or 
        check_diagonal_whoWins(renderboard)):
        drawrenderboard(renderboard)
        print(f"Player {whoWins} wins!")
        print("Game Over!")
        isGameInProgress = False

# Check for tie
def is_renderboard_full(renderboard):
    global isGameInProgress
    for rowNumber in renderboard:
        for colNumber in rowNumber:
            if colNumber == ' ':
                return False
    print("It's a tie!")
    isGameInProgress = False
    return True

# Switch player
def switch_player():
    global currentSymbol
    if currentSymbol == '+':
        currentSymbol = '-'
    else:
        currentSymbol = '+'

# Computer input
def computer_input(renderboard):  
    while currentSymbol == '+':
        rowNumber_position = random.randint(0, 2)
        rowNumber = rowNumber_position
        colNumber_position = random.randint(0, 2) 
        colNumber = colNumber_position
        if renderboard[rowNumber_position][colNumber_position] == ' ':
            renderboard[rowNumber][colNumber] = '-'
            switch_player()

# Intro
gameposition()

# Main loop
def main():
    while isGameInProgress:
        drawrenderboard(renderboard)
        if playerInput(renderboard):
            computer_input(renderboard)
            switch_player()
        check_win() 
        is_renderboard_full(renderboard)

main()
