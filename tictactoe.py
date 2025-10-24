# Tic-Tac-Toe Game

# global constants
X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9


def display_instruct():
    print('\nWelcome to the Tic-Tac-Toe Game!')
    print('You will make your move by entering a number, 0 - 8')
    print('The number will correspond to the board position:')
    print('     0 | 1 | 2')
    print('     3 | 4 | 5')
    print('     6 | 7 | 8\n')


def ask_yes_no(question): #str
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower() #str method
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question)) # str method convert to int
    return response


# determine who is X and who is O
def pieces():
    go_first = ask_yes_no('Do you want to go first? (y/n): ')
    if go_first == 'y':
        print('Then take the first move.  You will need it.')
        human = X
        computer = O
    else:
        print('You are brave... I will go first.')
        computer = X
        human = O
    return computer, human


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '-'*9)
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '-'*9)
    print('\t', board[6], '|', board[7], '|', board[8], '\n')


def legal_moves(board):
    # create a list of legal moves, simply a list of empty squares
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    # loop through each way to win
    for row in ways_to_win:
        # if there is not spot to move, then there is a winner
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winning_piece = board[row[0]]
            return winning_piece
    # check if any empty squares on the board
    # if no empty squares, game over; it is a tie
    if EMPTY not in board:
        return TIE
    # there is no winner or tie yet, then return None
    return None


def computer_move(board, computer, human):
    board = board[:]
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('I shall take square number', end=' ')
    # loop through all empty squares
    for move in legal_moves(board):
        # pretend â€“ move the piece to that square and then check
        board[move] = computer
        # if computer would move here, would the computer win?
        if winner(board) == computer:
            # yes, computer would win, then choose this
            print(move)
            return move
        # no, comp would not move, then undo this move
        board[move] = EMPTY

    # no one can win.  Then check next best thing,
    # check to see if I can block human move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # no one can win, then just pick the next open square.
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move


def human_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Your move? Enter 0-8: ', 0, NUM_SQUARES)
        if move not in legal:
            print('\nThat square is occupied.  Choose another.\n')
    print('Fine...')
    return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    if the_winner == computer:
        print('I, the computer have won')
    elif the_winner == human:
        print('You won.  You got lucky.')
    elif the_winner == TIE:
        print('It is a tie')


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    # loop while there is not a winner
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()