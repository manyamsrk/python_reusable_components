
def intialboard(board):

    print(board[1]+' | '+board[2]+' | '+board[3])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[7]+' | '+board[8]+' | '+board[9])

def replace_position(board,position,marker):
   # user_replacement = input('type a string to place at position')
    board[position] = marker
    return board

def welcome_msg():
    print('Welcome to Tic Tac Game')


def user_input_place(board,player):
    choice = 'wrong'
    while choice not in board:
        choice = input(f'Player{player} enter the placeholder (1-9):')
        if choice not in board:
            print(' sorry wrong placeholder')

    return int(choice)

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

def fullboardcheck(board):
    for i in range(1,10):
        if i not in board:
            return True
        else:
            return False


def user_input_choice():
    player1 = 'wrong'
    player2 = 'wrong'
    while player1 not in ['X', 'O']:
        player1 = input('Player1 - Enter the choice (X/O):').upper()
        if player1 not in ['X', 'O']:
            print('sorry wrong Choice')
        elif player1 == 'X':
            player2 = 'O'
            player1 = 'X'
        else:
            player2 = 'X'
            player1 = 'O'

    return player1, player2


board = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
gameon = True

while gameon:
    welcome_msg()
    intialboard(board)
    player1, player2 = user_input_choice()
    print(f'player1 choosed {player1}')
    print(f'player2 choosed {player2}')
    for i in range(1,10):

        if i%2 == 0:
            place = user_input_place(board,player='2')
            board = replace_position(board, place,player2)
            intialboard(board)
            if win_check(board,mark=player2):
                print('Player2 won the match')
                break
        else:
            place = user_input_place(board, player='1')
            board = replace_position(board, place, player1)
            intialboard(board)
            if win_check(board, mark=player1):
                print('Player1 won the match')
                break
    if fullboardcheck(board):
        gameon=False
