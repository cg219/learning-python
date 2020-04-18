player1 = None
player2 = None
moves = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
winningConditions = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def print_board():
    print(f" {moves[1]} | {moves[2]} | {moves[3]} ")
    print(f"---|---|---")
    print(f" {moves[4]} | {moves[5]} | {moves[6]} ")
    print(f"---|---|---")
    print(f" {moves[7]} | {moves[8]} | {moves[9]} ")

def which_player():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    return ("X", "O") if marker == 'X' else ("O", "X")

def clear_screen():
    for i in range(0,50):
        print("")

def make_move(player):
    move = 0
    global player1
    global player2

    clear_screen()
    print_board()

    while moves[move] != " ":
        move = int(input(f"({player}) make a move in an empty spot (1-9): "))

    moves[move] = player
    winner = check_game_status(player)

    if winner == "Tie":
        end_game("Tie")
    elif winner == player:
        end_game(player)
    else:
        make_move(player2) if player == player1 else make_move(player1)

def check_game_status(player):
    for x,y,z in winningConditions:
        if moves[x] == moves[y] == moves[z] == player:
            return player

    return "Tie" if " " not in moves else "Continue"

def start_game():
    global player1
    global player2

    print_board()
    player1, player2 = which_player()
    make_move(player1)

def end_game(condition):
    global player1
    global player2
    global moves

    clear_screen()
    print_board();
    moves = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    if condition == (player1 or player2):
        print(f"Player ({condition}) Wins!!")
    else:
        print("Tie Game! No one wins :(")

    if input('Would you like to play again?? (Y) or (N)').upper() == "Y":
        player1, player2 = which_player()
        make_move(player1)

start_game()

