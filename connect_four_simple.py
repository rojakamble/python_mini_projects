print("\n")
print("#####################################################")
print("########### WELCOME TO CONNECT FOUR GAME ############")
print("#####################################################")
print("\n")
print("Player 1 drops RED chip")
print("Player 2 drops YELLOW chip")
print("\n")

num_row = 6
num_col = 7

# 0 - no chips
# 1 - red chip
# 2 - yellow chip

board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

def printBoard():
    for row in range(0, num_row):
        for col in range(0, num_col):
            print(board[row][col], end=' ')
        print(" ")
 
print("\nEmpty board before game starts\n")       
printBoard()

def fillIn(col, player):
    col = col - 1
    for rows in range(num_row-1, -1, -1):
        if board[rows][col] == 0:
            print('\nlegal move\n')
            board[rows][col] = player
            break

def horizWin():
    for row in range(0, num_row):
        for col in range(0, 4):
            if board[row][col] > 0:
                 if board[row][col] == board[row][col+1] == \
                    board[row][col+2] == board[row][col+3]:
                        print('Player', board[row][col], 'won!')
                        return True
    return False
                
def vertWin():
    for row in range(0, 3):
        for col in range(0, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col] == \
                    board[row+2][col] == board[row+3][col]:
                        print('Player', board[row][col], 'won!')
                        return True
    return False

def diagBottomLeftToTopRightWin():
    # check for starting position of diagonal
    # going up and to the right
    for row in range(3, num_row):
        for col in range(0, 4):
            # print(row, col)
            if board[row][col] > 0:
                if board[row][col] == board[row-1][col+1] == \
                    board[row-2][col+2] == board[row-3][col+3]:
                        print('Player', board[row][col], 'won!')
                        return True
    return False

def diagTopLeftToBottomRightWin():
    
    # check for different starting position of diagonal
    # going down and to the right
    for row in range(0, 3):
        for col in range(0, 4):
            # print(row, col)
            if board[row][col] > 0:
                # print(row, col)
                # print(board[row][col], board[row+1][col+1],board[row+2][col+2], board[row+3][col+3])
                if board[row][col] == board[row+1][col+1] == \
                    board[row+2][col+2] == board[row+3][col+3]:
                        print('Player', board[row][col], 'won!')
                        return True
    return False

def win():
    if horizWin() or vertWin() or diagBottomLeftToTopRightWin() or diagTopLeftToBottomRightWin():
        return True
    return False

def game():
    player = 1 # 1 - red, 2 - yellow
    while not win():
        col = int(input('Enter a column: '))
        fillIn(col, player)
        printBoard()
        if player == 1:
            player = 2
        else:
            player = 1
        
if __name__ == "__main__":
    game()