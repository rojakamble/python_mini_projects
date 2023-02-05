print("\n")
print("#####################################################")
print("########## WELCOME TO **TIC TAC TOE** GAME ##########")
print("#####################################################")
print("\n")
print("Player 1 places X chip")
print("Player 2 places O chip")
print("\n")

ROWS = 3
COLS = 3

# assuming that board size will not increase
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0 ,0]]

def print_board():
    for row in range(0, ROWS):
        for col in range(0, COLS):
            print(board[row][col], end=" ")
        print()
 
print("Empty board before game starts\n")       
print_board()

def fill_board(row, col, player):
    
    if board[row][col] == 0:
        print('\nlegal move\n')
        board[row][col] = player
        
    else:
        print("Input is wrong, please check.")
        
        
def win_row_check():
    # print("\n I am in win_row_check")
    col = 0
    for row in range(0, ROWS):
        if board[row][col] > 0:
            if board[row][col] == board[row][col+1] == board[row][col+2]:
                print('\nPlayer', board[row][col], 'won!', 'Congrats!')
                return True
        
    return False
        
def win_col_check():
    # print(" I am in win_col_check")
    row = 0
    for col in range(0, COLS):
        if board[row][col] > 0:
            if board[row][col] == board[row+1][col] == board[row+2][col]:
                print('\nPlayer', board[row][col], 'won!', 'Congrats!')
                return True
            
    return False
        
def win_diagonal_left_check():
    # print(" I am in win_diagonal_left_check")
    row = 0
    col = 0
    if board[row][col] > 0:
        if board[row][col] == board[row+1][col+1] == board[row+2][col+2]:
            print('\nPlayer', board[row][col], 'won!','Congrats!')
            return True
    
    return False
    
def win_diagonal_right_check():
    # print(" I am in win_diagonal_right_check")
    row = 0
    col = 2
    if board[row][col] > 0:
        if board[row][col] == board[row+1][col-1] == board[row+2][col-2]:
            print('\nPlayer', board[row][col], 'won!', 'Congrats!')
            return True
        
    return False
    
def win():
    # print("I am in win block")
    if win_row_check() or win_col_check() or win_diagonal_left_check() or win_diagonal_right_check():
        return True
    else:
        return False
    
def game():
    player = 1 # 1 - X, 2 - O
    while not win(): 
       
        row = int(input('\nPick row to insert: '))
        col = int(input('\nPick col to insert: '))
        
        fill_board(row, col, player)
        
        if player == 1:
            print("Player 1 turn (X)")
            player = 2
        else:
            print("Player 2 turn (O)")
            player = 1
        
        print_board()
    
    print("\nThank you for playing! Hope you had fun! \n")
         

if __name__ == "__main__":
    game()
     
    