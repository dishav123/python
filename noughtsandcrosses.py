import random
import os.path
import json
random.seed()

def draw_board(board):
    print("-"*12)
    for row in range(3):
        for column in range(3):
            print(f'| {board[row][column]}',end=" ")
        print("|")
        print("-"*12)
    
    pass

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print("Welcome to 'Unbeateable nought and cross'game.")
    draw_board(board)
    pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j]=' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            print("When prompted, enter the number corresponding to the square you want.")
            user_input = int(input('Choose your square: \t1 2 3\n\t\t\t4 5 6\n\t\t\t7 8 9:'))
            if user_input == 1 and board[0][0] == ' ':
                row=0
                col=0
                return row, col
            elif user_input == 2 and board[0][1] == ' ':
                row=0
                col=1
                return row, col
            elif user_input == 3 and board[0][2] == ' ':
                row=0
                col=2
                return row, col
            elif user_input == 4 and board[1][0] == ' ':
                row=1
                col=0
                return row, col
            elif user_input == 5 and board[1][1] == ' ':
                row=1
                col=1
                return row, col
            elif user_input == 6 and board[1][2] == ' ':
                row=1
                col=2
                return row, col
            elif user_input == 7 and board[2][0] == ' ':
                row=2
                col=0
                return row, col
            elif user_input == 8 and board[2][1] == ' ':
                row=2
                col=1
                return row, col
            elif user_input == 9 and board[2][2] == ' ':
                row=2
                col=2
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError as e:
            print(f'<<ERROR OCCURED:>>',e)
            print("Please try again!!")

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    empty_box=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                empty_box.append((i,j))
    if (empty_box):
        #selects any random row and column from emptybox.
        choose=random.choice(empty_box)
        row=choose[0]
        col=choose[1]
        return row,col
    


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(3):
        #for row
        if all(board[i][j]==mark for j in range(3)):
            return True
        #for column
    for i in range(3):
        if all(board[j][i]==mark for j in range(3)):
            return True
        #for first diagonal 
    if all(board[i][i]==mark for i in range(3)):
        return True
        #for second digonal
    if all(board[i][2-i]==mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if (board[i][j]==' '):
                return False    
    return True

        
def play_game(board):
    # develop code to play the game
    # start with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    initialise_board(board)
    draw_board(board)
    
    while True:
        row,column=get_player_move(board)
        board[row][column]='X'
        draw_board(board)

        if check_for_win(board,"X"):
            print("Booyah!! you win")
            return 1
        if check_for_draw(board):
            print("Tie game,GG!")
            return 0
        
        computer_row,computer_column=choose_computer_move(board)
        board[computer_row][computer_column]='O'
        draw_board(board)

        if check_for_win(board,"O"):
            print("You lose!!!")
            return -1
        if check_for_draw(board):
            print("Tie game,GG!")
            return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    choice=input("Enter one of the following options.\n"
                "\t1-Play the game\n\t2-Save your in Leaderboard\n"
                "\t3-Load and display the leaderboard\n\tq-End the program\n1,2,3,q?:").lower()
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaderss()
    if os.path.exists("leaderboard.txt"):
        with open ("leaderboard.txt","r") as file:
            leaders={}
            lines=file.readlines()
            for line in lines:
                key,value=line.split(':')
            leaders[key]=value
        return leaders
    else:
        print("file doesn't exist!!!")
    
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name=input("Enter your name:")
    with open("leaderboard.txt", "w") as file:
        file.write(f'{name}:{score}\n')
        print("Your score has been saved in leaderboard.txt!\n")
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    for key, value in leaders.items():
        print(f'Hey {key}!, your highest score is {value}.')
    pass

def main():
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]
    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

main()

