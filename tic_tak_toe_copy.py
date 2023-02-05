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

dict_values = { "1" : [0, 0],
                "2" : [0, 1],
                "3" : [0, 2],
                "4" : [1, 0],
                "5" : [1, 1],
                "6" : [1, 2],
                "7" : [2, 0],
                "8" : [2, 1],
                "9" : [2, 2]}

def print_board():
    for row in range(0, ROWS):
        for col in range(0, COLS):
            print(board[row][col], end=" ")
        print()
 
print("Empty board before game starts\n")       
print_board()

def fill_board1(pos, player):
    
    if int(pos) < 10:
        if dict_values[pos]:
            print('\nlegal move\n')
            row = dict_values[pos][0]
            col = dict_values[pos][1]
            board[row][col] = player
            return True
    print("Input is wrong, please check.")
    return False

def fill_board2(pos, player):

    if pos.isdigit() and int(pos) < 10 and int(pos) > 0:
        row = (int(pos)-1) // 3
        col = (int(pos)-1) % 3
        if board[row][col] == 0:
            print('\nlegal move\n')
            board[row][col] = player
            return True
    else:
        print("Enter a number between 1-9.")
    print("Input is wrong, please check.")
    return False
    
        
        
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
    elif game_over():
        quit()
    else:
        return False

def game_over():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
        
    print("*** GAME OVER ***") 
    return True  
            
                
    
def game():
    player = 1 # 1 - X, 2 - O
    while not win(): 
       
        pos = input(f"\n Player {player} Enter a position to insert: ")
        
        fill_board2(pos, player)
        
        if player == 1:
            player = 2
        else:
            player = 1
        
        print_board()
    
    print("\nThank you for playing! Hope you had fun! \n")
         

if __name__ == "__main__":
    game()
     
    