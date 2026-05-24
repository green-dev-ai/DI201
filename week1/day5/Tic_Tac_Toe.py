# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def play():
    """ this is the main game flow function """
    
    valid = False
    while valid is False:
        row, col = get_play(player)
        valid = check_valid(row, col)
    update_board(row, col, player)
    create_board(game_board)
    player = switch_player(player)
      

def update_board(row, col, player):
    """this function updates the board with the value of X or O"""
    if player == "A":
        game_board[(row-1, col-1)] = "X"
    else:
        game_board[(row-1, col-1)] = "O"
    print(f"{game_board[(row, col)]}{row-1}{col-1}")

def switch_player(player):
    """this function alternates between the players after every valid turn"""
    if player == "A":
        return "B"
    else:
        return "A"

def get_play(player):
    """this is the function to get players input"""  
    row = int(input(f"Player {player} (X) - enter the row of you play (1-3):"))
    col = int(input(f"Player {player} (X) - enter the column of you play (1-3):"))
    return row, col
    
def create_board(game_board):
    """this function creates the new board of play"""
    i = 0
    while i < 3:
        print(f"|---|---|---|")
        print(f"| {game_board[(i,0)]} | {game_board[(i,1)]} | {game_board[(i,2)]} |")
        i += 1    
    print(f"|---|---|---|")

def check_win(player):
    """this function check to see if any player won"""
    for i in range(0,2):
        if game_board[(i, 0)] == game_board[(i, 1)] == game_board[(i, 2)] != " ":
            return True
        if game_board[(0, i)] == game_board[(1, i)] == game_board[(2, i)] != " ":
            return True
    
#        if game_board[(0,0)] == game_board[(1,1)] == game_board[(2,2)] != " ":
#        return True

#   if game_board[(0,2)] == game_board[(1,1)] == game_board[(2,0)] != " ":
#        return True
#    elif   need to check in alchson both ways
    return False

def check_tie():
    """this function checks to see if all the spots have been played"""
    if " " not in game_board.values():
        print(f"the game is tied.")

def check_valid(row, col):
    """this check the validity of the input and return True if valid"""
    if 1<= row <=3 and 1 <= col <=3:
        if game_board[(row-1, col-1)] == "X" or game_board[(row-1, col-1)] == "O":
            print(f"this cell is already taken")
            return False
        else:
            print(f"here")
            print(f"{game_board[(row-1, col-1)]}")
            return True
    else:
        print(f"enter a valid row and acolumn between 1 and 3 for ")
        return False




game_board = {}
for row in range(3):
    for col in range(3):
        game_board[(row,col)] = " "
create_board(game_board)
player = "A"

while check_win(player) is False:
    play()
print(f"Player {player} Won !!!")



