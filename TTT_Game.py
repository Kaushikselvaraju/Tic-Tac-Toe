from random import choice
combo_indices = [
    [0, 1, 2 ,3 ,4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13,14],
    [15, 16, 17, 18, 19],
    [20, 21, 22,23,24],
    [0, 5, 10,15,20],
    [1, 6, 11,16,21],
    [2,7,12,17,22],
    [3,8,13,18,23],
    [4,9,14,19,24],
    [0,6,12,18,24],
    [4,8,12,6,20]
]
EMPTY_SIGN = '.'
N = input("Choose X or O:  ")
t = 0
if N == "X":
    USER_SIGN, CPU_SIGN = 'X', 'O'
    t=1
elif N == "O":
    USER_SIGN, CPU_SIGN = 'O', 'X'
    t=1
else:
    print("Choose only character X or O")
def print_board(board):
    print(" ")
    print(' '.join(board[:5]))
    print(' '.join(board[5:10]))
    print(' '.join(board[10:15]))
    print(' '.join(board[15:20]))
    print(' '.join(board[20:25]))
    print(' '.join(board[25:]))
    print(" ")
def opponent_move(board, row, column):
    index = 5 * (row - 1) + (column - 1)
    if board[index] == EMPTY_SIGN:
        return board[:index] + USER_SIGN + board[index+1:]
    return board
def every_moves(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            move_list.append(board[:i] + sign + board[i+1:])
    return move_list
def cpu_move(board):
    return choice(every_moves(board, CPU_SIGN))
def game_won_by(board):
    for index in combo_indices:
        if board[index[0]] == board[index[1]] == board[index[2]] == board[index[3]] == board[index[4]] != EMPTY_SIGN:
            return board[index[0]]
    return EMPTY_SIGN
def game_over():
    board = EMPTY_SIGN * 25
    empty_cell_count = 25
    is_game_ended = False
    while empty_cell_count > 0 and not is_game_ended:
        if empty_cell_count % 2 == 1:
            board = cpu_move(board)
        else:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            board = opponent_move(board,   row, col)
        print_board(board)
        is_game_ended = game_won_by(board) != EMPTY_SIGN
        empty_cell_count = sum(1 for cell in board if cell == EMPTY_SIGN)
    print('Game has been ended.')
    print('Congrats you won ;)')
if t==1:
    game_over()
