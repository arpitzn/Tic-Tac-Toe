# ------- Global Variable --------
# Game board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#If game is still going 
game_still_going = True

#who won ? or tie ?
winner = None

#whose turn is it 
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8]) 

#play a game of tic tac toe
def play_game():
    #display initial board
    display_board()
    #while the game is still going
    while game_still_going:
        #handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        #check if the game has ended
        check_if_game_over()

        #flip to the other player 
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.") 
    elif winner == None:
        print("Tie.")      
            
      

#handle a single turn of an arbitray player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
            board[position] = player
        else:    
            print("You can't go their, Go again")
            print(player + "'s turn.")


        # board[position] = player

        display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie() 

def check_for_winner():
    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    # check coloumns
    coloumn_winner = check_coloumns()
    # check diagonals
    diagonal_winner = check_diagonals() 
    
    if row_winner:
        #there was a win
        winner = row_winner
    elif coloumn_winner:
        #there was a win
        winner = coloumn_winner
    elif diagonal_winner:
        #there was a win 
        winner = diagonal_winner
    else:
        #there was no win
        winner = None   
        
    return    

def check_rows():
    #set up global variable
    global game_still_going
    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner(X or O)
    if row_1:
        return board[0]
    elif row_2:    
        return board[3]
    elif row_3:
        return board[6]
            
    return

def check_coloumns():
    #set up global variable
    global game_still_going
    # check if any of the rows have all the same values (and is not empty)
    coloumn_1 = board[0] == board[3] == board[6] != "-"
    coloumn_2 = board[1] == board[4] == board[7] != "-"
    coloumn_3 = board[2] == board[5] == board[8] != "-"

    #if any row does have a match, flag that there is a win
    if coloumn_1 or coloumn_2 or coloumn_3:
        game_still_going = False
    # return the winner(X or O)
    if coloumn_1:
        return board[0]
    elif coloumn_2:    
        return board[1]
    elif coloumn_3:
        return board[2]
    return

def check_diagonals():
    #set up global variable
    global game_still_going
    # check if any of the rows have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner(X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:    
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #gloabal variable we need
    global current_player
    #if global variable is X then change it to O
    if current_player == "X":
        current_player = "O"
    #if global variable is O then change it to X  
    elif current_player == "O":
        current_player = "X"
    return     

play_game()   

